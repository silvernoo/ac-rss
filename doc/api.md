### Acfun channel api

http://api.acfun.tv/apiserver/content/channel?orderBy=1&channelId=110&pageSize=20&pageNo=1

key			|value
------------|------
orderBy		|顺序
channelId	|频道Id
pageSize	|单页条目数量
pageNo		|页数

### 更新规则

每2小时更新一次本地文件

RRS条目只存在10个

> \* */2 * * * /root/acfun_check.py