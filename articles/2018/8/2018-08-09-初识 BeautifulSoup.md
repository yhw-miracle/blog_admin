BeautifulSoup 是一个可以从 HTML 或 XML 文件中提取数据的 python 库，它能通过解析器实现文档的查找提取和修改等功能。

### BeautifulSoup 的安装
对于 BeautifulSoup，目前推荐使用的是 BeautifulSoup 4，BeautifulSoup 3　已经停止开发了。安装 BeautifulSoup 4 有四种方式。

> * 最新版的 Debain 或 Ubuntu 系统可以通过系统的软件包管理来安装，sudo apt-get install Python-bs4。
> * BeautifulSoup 4 通过 PyPi 发布，可以通过 easy_install 或 pip 来安装，easy_install beautifulsoup4　或 pip install beautifulsoup4。
> * 通过源码安装，BeautifulSoup 4 的源码地址为[https://pypi.python.org/pypi/beautifulsoup4/](https://pypi.python.org/pypi/beautifulsoup4/)，下载源码，解压后，运行命令 python setup.py install 即可完成安装。
> * 通过 PyCharm　里 Project Interpreter 安装 BeautifulSoup 4。

![](images/2018/August/Screenshot%20from%202018-08-09%2012-55-42.png)

BeautifulSoup 支持 Python 标准库中的 HTML 解析器，还支持一些第三方解析器，如，lxml，html5lib 等，安装这些解析器方法与安装 BeautifulSoup 4 类似。

| 解析器 | 优势 | 劣势 |
| ------ | ------ | ------ |
| Python 标准库 | Python 的内置标准库，执行速度适中，文档容错能力强 | Python 早期版本文档容错能力差 |
| lxml HTML 解析器 | 速度快，文档容错能力强 | 需要安装 C 语言库 |
| lxml xml 解析器 | 速度快，唯一支持 xml 的解析器 | 需要安装 c　语言库 |
| html5lib | 最好的容错性，以浏览器方式解析文档，生成 HTML5 格式的文档 | 速度慢，不依赖外部扩展 |

### BeautifulSoup 的使用
BeautifulSoup 将复杂的 HTML 文档转换成一个复杂的树形结构，每个节点是 python 对象，这些对象可以归纳为 Tag、NavigableString、BeautifulSoup、Comment。

```html
<!-- 测试文档　-->
<html><head><title>my blog</title></head>
<body>
<p class="title"><b>One</b></p>
<p class="story">Two
<a href="http://xxx.cn/one" class="one" id="link1"><!-- one --></a>,
<a href="http://xxx.cn/two" class="two" id="link2"><!-- two --></a> and
<a href="http://xxx.cn/three" class="three" id="link3">three</a>;
hello,world</p>
<p class="story">...</p>
```

#### Tag 对象
Tag 对象可以直接以标签名获取标签内容，Tag 对象还有两个属性 name 和 attr，分别表示获取到标签的名称和标签属性内容（以字典的形式返回）。

```python
# coding:utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlStr, 'lxml', from_encoding='utf-8')
print(soup.a)
print(type(soup.a))
print(soup.a.name)
print(soup.a.attrs)
```

![](images/2018/August/Screenshot%20from%202018-08-10%2014-18-03.png)

#### NavigableString 对象
NavigableString 对象用来获取标签内部字符串，利用属性 string 来获取。

```python
# coding:utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlStr, 'lxml', from_encoding='utf-8')

print(soup.p.string)
print(type(soup.p.string))
```

![](images/2018/August/Screenshot%20from%202018-08-10%2014-24-18.png)

#### BeautifulSoup 对象
BeautifulSoup 对象表示一个文档的全部内容，可以理解为特殊的 Tag 对象。

```python
# coding:utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlStr, 'lxml', from_encoding='utf-8')

print(soup.name)
print(type(soup.name))
```

![](images/2018/August/Screenshot%20from%202018-08-10%2014-29-25.png)

#### Comment 对象
Commnet 对象用来获取文档中注释的内容。

```python
# coding:utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlStr, 'lxml', from_encoding='utf-8')

print(soup.a.string)
print(type(soup.a.string))
```

![](images/2018/August/Screenshot%20from%202018-08-10%2014-32-08.png)

#### BeautifulSoup 支持文档树遍历，可以根据子节点、父节点、兄弟节点和前后节点进行遍历。

| 遍历方面 | 属性描述 |
| ------ | ------ |
| 子节点 | .contents, .children, .descendants |
| 父节点 | .parent, .parents |
| 兄弟节点 | .previous_sibling(s), .next_sibling(s) |
| 前后节点 | .previous_element(s), .next_element(s) |

BeautifulSoup 还支持 find*() 方法搜索文档树，以及支持 select() 方法根据　CSS 选择器查找文档中指定的标签。
