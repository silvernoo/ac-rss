#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

header = {
    "acPlatform": "ANDROID_PHONE",
    "User-agent": "acvideo core/5.13.0.635(Xiaomi;MI 5;7.0)",
    "deviceType": "1",
    "uuid": "2752386c-f4fc-4068-b358-ad86a2d6377d",
    "Cookie": "did=ddd824e2-dc17-38c2-97b1-6de8d1f44af2",
    "appVersion": "5.13.0.635",
    "market": "tencent",
    "productId": "2000",
    "uid": "0",
    "resolution": "1080x1920",
    "udid": "ddd824e2-dc17-38c2-97b1-6de8d1f44af2",
    "requestTime": "2019-01-30 16:36:12.447",
    "Host": "apipc.app.acfun.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}


def get_all_channel():
    request = requests.get(url="http://apipc.app.acfun.cn/v3/channels/allChannels", headers=header)
    json = request.json()
    article_ = json["vdata"]["article"]
    result = {}
    for item in article_:
        lst = []
        for realm in item["realm"]:
            lst.append(str(realm["id"]))
        result.update({item["id"]: item["name"] + "$$" + ",".join(lst)})
    return result

if __name__ == "__main__":
    channel = get_all_channel()
    print(channel)
