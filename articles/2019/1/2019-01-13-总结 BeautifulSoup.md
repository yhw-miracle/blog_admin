1. BeautifulSoup4 支持 python 标准库(html.parser)、lxml、html5lib 这些解析器解析文档。

2. 格式化输出文档内容 print soup.prettify()，会自动补全文档。

3. BeautifulSoup4 将复杂的 html 文档转换成一个复杂的树形结构，每一个节点是 python 对象，所有的对象有四种：Tag、NavigableString、BeautifulSoup、Comment。

4. Tag 查找的是文档中第一个符合内容的标记，有两个属性：name 和 attrs，分别为获取标记的名称和属性，.attrs 返回的是字典类型，也可以用 [] 和 get() 来获取特定的属性内容。

5. NavigableString 表示的是标记内部的字符串，可以用 .string 来获取。

6. BeautifulSoup 表示的是文档的全部内容，.name 返回的是 [document]，.attrs 返回的是 {}。

7. Comment 表示的是文档的注释内容，用 .string 可以获取去掉注释符号的注释内容，可以用 type() == bs4.element.Comment 来判断该字符串是否为注释。

8. BeautifulSoup 将 html 文档转换为文档树，支持子节点、父节点、兄弟节点和前后节点进行遍历文档树。

9. 获取子节点的属性有 contents、children、descendants。contents 以列表的形式返回直接子节点信息；children 返回的是直接子节点迭代器，可以用 for in 循环遍历；descentants 返回的子孙节点迭代器，可以用 for in 循环遍历。

10. 获取子节点内容的属性有 string、strings、stripped_strings。string 返回的是标记最内部的内容；strings 返回的是标记内部字符串的迭代器，可以用 for in 循环遍历，包括空格和换行；stripped_string 是去掉 strings 中的空格和换行。

11. 获取节点的父节点的属性是 parent，获取节点的父辈节点的属性是 parents，返回父辈节点的迭代器，可以使用 for in 循环遍历。 

12. 获取节点的兄弟节点的属性有 next_sibling，next_siblings 和 previous_sibling，previous_siblings。节点的兄弟节点包括字符串节点（字符串、空格、换行）。

13. 获取节点的前后节点的属性有 next_element，next_elements 和 previous_element，previous_elements。同样前后节点也包括字符串节点。

14. 搜索文档树的方法主要是一系列 find 方法，以列表的形式返回。以 find_all(name, attrs, recursive, text, limit, **kwargs) 为例，其中 name 参数以节点的名称来搜索文档树；attrs 参数以节点的属性信息来搜索文档树，以字典形式给出；text 参数以节点的内容来搜索文档树；kwargs 参数可以以不是 python 内置的关键字参数来搜索文档树，包括标记的 class 属性，id 属性等。name、attrs、text、kwargs 参数支持字符串、正则表达式、列表、TRUE（匹配任何值）。recursive 参数为 False 时，BeautifulSoup 会搜索直接子节点，limit 会限制 BeautifulSoup 搜索节点的个数。

15. BeautifulSoup 还支持 CSS 语法来搜索文档树，使用的方法是 select()，返回的类型是列表类型。