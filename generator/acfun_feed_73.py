# -*- coding: utf-8 -*-  
import datetime
import PyRSS2Gen
import json
import requests

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#工作·情感
if __name__ == '__main__':
    headers = {
        'appVersion': '4.2.1',
        'User-agent': 'acvideo core',
        'market': 'tencent',
        'productId': '2000',
        'deviceType': '1',
        'uid': '0',
        'resolution': '1440x2392',
        'udid': '6efe5b7d-ea2d-3985-a46b-32732b5d45ad',
        'Host': 'api.aixifan.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    response = requests.get('http://api.aixifan.com/searches/channel?channelIds=73&pageNo=1&pageSize=20&sort=4',
                            headers=headers)
    x_content = json.loads(response.content)
    items = []
    list = x_content['data']['list']
    for i in range(0, len(list)):
        item_json = list[i];
        items.append(PyRSS2Gen.RSSItem(
            title=item_json['title'],
            link='http://www.acfun.tv/a/ac' + str(item_json['contentId']),
            description=item_json['description'],
            guid=PyRSS2Gen.Guid('http://www.acfun.tv/a/ac' + str(item_json['contentId'])),
            pubDate=datetime.datetime.fromtimestamp(int(str(item_json['releaseDate'])[:-3])).strftime('%Y-%m-%d %H:%M:%S')))

    rss = PyRSS2Gen.RSS2(
        title='Acfun 文章区',
        link='http://www.acfun.tv/v/list73/index.htm',
        description='Acfun 文章区',
        lastBuildDate=datetime.datetime.now(),
        items=items)
    rss.write_xml(open('feed_73.xml', 'w'), encoding='utf-8')