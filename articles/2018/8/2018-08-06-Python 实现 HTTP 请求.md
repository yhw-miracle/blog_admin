python　中实现 HTTP 请求有三种方式，分别为 urllib2/urllib、httplib/urllib 和 Requests。

### urllib2/urllib
#### 基本请求和响应模型
urllib2 和 urllib 是 Python 中的两个内置模块，实现 HTTP 请求时，以 urllib2 为主，urllib　为辅。urllib2 模块提供了 urliopen() 方法，可以向指定的 URL 发出请求来获取数据。

```python
# coding:utf-8

import urllib2

# 请求
request = urllib2.Request('http://www.baidu.com')

# 响应
response = urllib2.urlopen(request)

print response.read()
```

#### 请求头 headers 处理
请求头信息可以直接与 URL 一起放到 Requset() 方法里，也可以使用 add_header() 方法添加请求头信息。

```python
# coding:utf-8

import urllib2
import urllib

url = "https://github.com/login"
userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'https://github.com'
postData = {'username': '111', 'passowrd': '222'}

# 将 userAgent, referer 写入头信息
headers = {'User-Agent': userAgent, 'Referer': referer}

data = urllib.urlencode(postData)
request = urllib2.Request(url, data, headers)
# request.add_header('User-Agent', userAgent)
# request.add_header('Referer', referer)
response = urllib2.urlopen(request)
print response.read()
```

#### Cookie 处理
urllib2 对 Cookie 的处理是自动的，使用 CookieJar 函数进行 Cookie 的管理。我们也可以通过设置请求头中的 Cookie 域来自定义添加 Cookie 的内容。

```python
# coding:utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    print item.name + ':' + item.value
```

```python
# coding:utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener()
opener.addheaders.append(('cookie', 'email='+"xxx@163.com"))
request = urllib2.Request('http://www.baidu.com')
response = opener.open(request)
print response.headers
print response.read()
```

#### 设置超时处理的三种方法
在 python2.6 之前的版本，urllib2 的 API 并没有 Timeout 的设置，要设置 Timeout 值，只能通过设置 Socket 的全局 Timeout 值实现。而在 python2.6 及新的版本中，urlopen() 函数提供了对 Timeout 的设置。

```python
# coding:utf-8

import urllib2
import socket

# way 1
socket.setdefaulttimeout(10)

# way 2
urllib2.socket.setdefaulttimeout(10)

# way 3
request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request, timeout=2)
print response.read()
```

#### 获取 HTTP 响应码
对于 200 OK 来说，urlopen() 方法返回的 response 对象的 getcode() 方法可以得到该 HTTP 响应码，但是对于其他类型的响应码，urlopen() 方法会抛出异常，这样需要通过异常对象来获取响应码。

```python
# coding:utf-8

import urllib2

response = urllib2.urlopen('http://www.baidu.com')
print response.getcode()

try:
    response = urllib2.urlopen('http://www.google.com', timeout=10)
    print response
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print 'Error code:', e.code
```

#### 重定向
urllib2 默认情况下会针对 HTTP 3XX 返回码自动进行重定向动作。要检测是否发生了重定向动作，只要检查一些 Response 的 URL 和 Resquest 的 URL 是否一致就可以了。

```python
# coding:utf-8

import urllib2

response = urllib2.urlopen('http://www.zhihu.com')
isRedirected = response.geturl() == 'http://www.zhihu.com'
print isRedirected
```

如果不想自动重定向，可以自定义 HTTPRedirectHandler 类实现。

```python
# coding:utf-8

import urllib2


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result


opener = urllib2.build_opener(RedirectHandler)
opener.open('http://www.zhihu.com')
```

#### Proxy 代理
urllib2 默认使用环境变量 http_proxy 来设置 HTTP Proxy；也可以使用 ProxyHandler 在程序中动态设置代理。

```python
# coding:utf-8

import urllib2

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener([proxy, ])
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.zhihu.com')
print response.read()
```

使用 urllib2.install_opener() 方法会全局设置代理，不利于更细粒度的控制，可以使用 opener.open() 代替全局的 urlopen()　方法使用不同的代理。

```python
# coding:utf-8

import urllib2

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy, )
response = opener.open('http://www.zhihu.com')
print response.read()
```

### httplib/urllib
httplib 模块是一个底层基础模块，可以了解建立 HTTP 请求的每一步，正常情况下开发用的很少。

| 功能 | API |
| ------ | ------ |
| 创建 HTTPConnection 对象 | httplib.HTTPConnection(host[.port,[strict[,timeout[,source_address]]]]) |
| 发送请求 | HTTPConnection.request(method,url[,body[,headers]]) |
| 获得响应 | HTTPConnection.getresponse() |
| 读取响应信息 | HTTPResponse.read() |
| 获取指定请求头信息 | HTTPResponse.getheader(name[,default]) |
| 获取响应头，以 (header, value) 元组构成的列表返回 | HTTPResponse.getheaders() |
| 获取底层 socket 文件描述符 | HTTPResponse.fileno() |
| 获取头内容 | HTTPResponse.msg |
| 获取头 http 版本 | HTTPResponse.version |
| 获取返回状态码 | HTTPResponse.status |
| 获取返回说明 | HTTPResponse.reason |

### Requests
#### Requests 安装
Python 中 Requests 模块实现 HTTP　请求的方式非常简单，操作更加人性化。Requests 库是第三方模块，需要额外安装，其源码开源，位于 [Github](https://github.com/requests/requests) 上。安装 requests 方式有两种：

> 1. 直接在 Terminal 上输入命令 pip install requests
> 2. 下载 [requests 源码](https://github.com/requests/requests/releases)，然后解压，在 Terminal 中进入解压后的目录，运行 setup.py 文件即可。

#### 基本请求和响应模型

```python
# coding:utf-8

import requests

# get 请求
req = requests.get('http://www.baidu.com')
print(req.content)

# post 请求
postData = {'key': 'value'}
req = requests.post('http://www.xxx.com/login', postData)
print(req.content)

# https://zzk.cnblogs.com/s/blogpost?Keywords=blog:qiyeboy&pageindex=1
# 处理 ? 后面的参数
payload = {'Keywords': 'blog:qiyeboy', 'pageindex': 1}
req = requests.get('https://zzk.cnblogs.com/s/blogpost', params=payload)
print(req.url)
```

#### 响应码 code 和请求头 headers 处理
```python
import requests

req = requests.get('http://www.baidu.com')
if req.status_code == requests.codes.ok:
    print(req.status_code)   # 响应码
    print(req.headers)   # 响应头
    print(req.headers.get('content-type'))
    print(req.headers['content-type'])
else:
    req.raise_for_status()
```

#### Cookie 处理
```python
import requests

userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': userAgent}
req = requests.get('http://www.baidu.com', headers=headers)
for cookie in req.cookies.keys():
    print(cookie + ':' + req.cookies.get(cookie))

userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': userAgent}
cookies = dict(name='qiye', age='10')
# 发送 cookie
req = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)

loginUrl = 'http://www.xxx.com/login'
s = requests.session()
# 首先访问登录页面，作为游客，服务器会先分配一个 cookie
req = s.get(loginUrl, allow_redirects=True)
datas = {'name': 'qiye', 'passwd': 'qiye'}
# 向登录链接发送 post 请求，验证成功，游客权限转为会员权限
req = s.post(loginUrl, data=datas, allow_redirects=True)
print(req.text)
```

#### 重定向与历史信息
```python
import requests

# allow_redirects=True 允许重定向，默认允许
# requests.get('', allow_redirects=True)
req = requests.get('http://github.com')
print(req.url)
print(req.status_code)
print(req.history)
```

#### 超时设置
```python
import requests

print(requests.get('http://www.google.com', timeout=5).content)
```

#### 代理设置
```python
import requests

proxies = {
    "http": "http://0.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
requests.get('http://example.org', proxies=proxies)
```

