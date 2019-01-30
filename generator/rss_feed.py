#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import PyRSS2Gen
import threading
import requests
from generator.all_channel import get_all_channel


def rss_parse(thread_id, r_ids):
    headers = {
        "acPlatform": "ANDROID_PHONE",
        "User-agent": "acvideo core/5.13.0.635(Xiaomi;MI 5;7.0)",
        "deviceType": "1",
        "uuid": "326f52e8-63ad-448d-8be7-5b3c75db85d3",
        "Cookie": "did=ddd824e2-dc17-38c2-97b1-6de8d1f44af2",
        "appVersion": "5.13.0.635",
        "market": "tencent",
        "productId": "2000",
        "uid": "0",
        "resolution": "1080x1920",
        "udid": "ddd824e2-dc17-38c2-97b1-6de8d1f44af2",
        "requestTime": "2019-01-30 16:36:16.928",
        "Host": "apipc.app.acfun.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    params = {
        "channelId": thread_id,
        "day": -1,
        "sort": 5,
        "realmIds": r_ids.split("$$")[1],
        "pageNo": 1,
        "pageSize": 10,
    }
    resp = requests.get("http://apipc.app.acfun.cn/v3/regions/search",
                        headers=headers,
                        params=params)
    json = resp.json()
    items = []
    list = json["vdata"]["list"]
    for item in list:
        items.append(PyRSS2Gen.RSSItem(
            title=item["channel"]["name"],
            link="http://www.acfun.tv/a/ac" + item["href"],
            guid=PyRSS2Gen.Guid("http://www.acfun.cn/a/ac" + item["href"]),
            pubDate=datetime.datetime.fromtimestamp(item["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S")))

    rss = PyRSS2Gen.RSS2(
        title="Acfun-文章区-%s" % r_ids.split("$$")[0],
        link="http://www.acfun.cm/v/list%d/index.htm" % thread_id,
        lastBuildDate=datetime.datetime.now(),
        description="Acfun-文章区-%s" % r_ids.split("$$")[0],
        items=items)
    save_file = "./rrs/feed_%d.xml" % thread_id
    rss.write_xml(open(save_file, "w", encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    channel = get_all_channel()
    for k, v in channel.items():
        threading.Thread(target=rss_parse, args=(k, v,)).start()
