# -*- coding: utf-8 -*-  
import datetime
import PyRSS2Gen
import simple_http
import json

if __name__ == '__main__':
    header, content = simple_http.get('http://api.acfun.tv/apiserver/content/channel?orderBy=1&channelId=110&pageSize=20&pageNo=1')
    x_content = json.loads(content)
    items = []
    list = x_content['data']['page']['list']
    for i in range(0, len(list)):
        item_json = list[i];
        items.append(PyRSS2Gen.RSSItem(
                title=item_json['title'],
                link='http://www.acfun.tv/a/ac' + str(item_json['contentId']),
                description=item_json['description'],
                guid=PyRSS2Gen.Guid('http://www.acfun.tv/a/ac' + str(item_json['contentId'])),
                pubDate=datetime.datetime.now()))
    
    rss = PyRSS2Gen.RSS2(
        title='Acfun 文章区',
        link='http://www.acfun.tv/v/list110/index.htm',
        description='Acfun 文章区',
        lastBuildDate=datetime.datetime.now(),
        items=items)
    rss.write_xml(open("D:\\feed.xml", "w"), encoding="utf-8")
