# -*- coding: utf-8 -*-  
from com import simple_http
import json
import xml.dom.minidom
import time
ISOTIMEFORMAT = '%Y-%m-%d %X'
if __name__ == '__main__':
    header, content = simple_http.get('http://api.acfun.tv/apiserver/content/channel?orderBy=1&channelId=110&pageSize=20&pageNo=1')
    x_content = json.loads(content)
    doc = xml.dom.minidom.Document();
    
    rss = doc.createElement('rss')
    doc.appendChild(rss);
    
    rss.setAttribute('version', '2.0')
    rss.setAttribute('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
    rss.setAttribute('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    channel = doc.createElement('channel')
    rss.appendChild(channel);
    
    root_title = doc.createElement('title')
    root_title.appendChild(doc.createTextNode('Acfun文章区'))
    root_link = doc.createElement('link')
    root_link.appendChild(doc.createTextNode('http://www.acfun.tv/v/list110/index.htm'))
    root_language = doc.createElement('language')
    root_language.appendChild(doc.createTextNode('zh-cn'))
    channel.appendChild(root_title)
    channel.appendChild(root_link)
    channel.appendChild(root_language)
    
    root_pubdate = doc.createElement('pubDate')
    root_pubdate.appendChild(doc.createTextNode(time.strftime(ISOTIMEFORMAT, time.localtime())))
    channel.appendChild(root_pubdate)
    
    list = x_content['data']['page']['list']
    for i in range(0, len(list)):
        bean = list[i]
        i_item = doc.createElement('item')
        channel.appendChild(i_item)
        i_title = doc.createElement('title')
        i_title.appendChild(doc.createTextNode(bean['title']))
        i_link = doc.createElement('link')
        i_link.appendChild(doc.createTextNode('http://www.acfun.tv/a/ac' + str(bean['contentId'])))
        i_description = doc.createElement('description')
        i_description.appendChild(doc.createTextNode(bean['description']))
        i_item.appendChild(i_title)
        i_item.appendChild(i_link)
        i_item.appendChild(i_description)
        
    print doc.toprettyxml(encoding='utf-8')