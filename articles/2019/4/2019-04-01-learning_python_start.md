### 初识 Python
* 在 python 控制台键入`import this`看 python 告诉我们的话：

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

* python 是解释型编程语言。
* python 中单行注释: `#`。
* python 中多行注释: 一对三引号，即`"""`和`"""`。
* python 中提供`todo`功能，在代码中注明`# TODO`即可。

### 变量
* 变量用于描述计算机中的数据存储空间，作用是在计算机内存中动态地保存数据。
* 变量名的命名规则是由**数字、字母和下划线**组成，不能以数字开头，不能是关键字，区分大小写。
* 变量的书写规范有下划线连接，驼峰命名法等
> 如
> ```python
> demo_demo = 1
> demoDemo = 2
> DemoDemo = 3
>```
* 查看 python 中关键字可用下面的语句，运行结果如图所示。
> ```python
> import keyword
> print(keyword.kwlist)
> ```

![](images/2019/Apr/01.png)

### 标准输入输出
* 输入：`input()`

* 输出：`print()`
	* %s，字符串占位符
	* %d，整数占位符
	* %f，浮点数占位符
	* %%，输入\%\

### python运算
* 字符串运算
	* `+`：拼接
	* `*`：连续拼接

* 算术运算符
	* `+`，加
	* `-`，减
	* `*`，乘
	* `/`，除
	* `/`，整除
	* `%`，取余
	* `**`，乘方
	* 优先级，乘方 > [乘，除，整除，取余] > [加，减]

* 赋值运算符
	* `=`，赋值
	* `+=`，加后赋值
	* `-=`，减后赋值
	* `*=`，乘后赋值
	* `/=`，除后赋值
	* `//=`，整除后赋值
	* `%=`，取余后赋值
	* `**=`，次方后赋值

* 比较运算符
	* `>`，大于
	* `>=`，大于等于
	* `<`，小于
	* `<=`，小于等于
	* `!=`，不低于
	* `==`，等于
	> 如何比较字符大小？
	> * 查看字母和数字的ASCII值；
	> * 查看指定字符的 ASCII 值：`ord()`；
	> * 已知 ASCII 值查看对应的字符：`chr()`。
	> <hr />
	> ```ipython
	> In [1]: ord('a')
	> Out[1]: 97
	> In [2]: chr(97)
	> Out[2]: 'a' 
	> ```

* 关系运算符（逻辑运算符）
	* `and`：短路与，若左操作数为 False，表达式结果为 False，。 
	* `or`：短路或，若左操作数为 True ，表达式结果为 True。
	* `not`：取反操作。
	* 一些例子：

	| 表达式 | 结果 |
	| ------ | ------ |
	| 1 and True | True |
	| 0 and True | 0 |
	| 1 or True | 1 |
	| 0 or True | True |
	| 1 and False | False |
	| 0 and False | 0 |
	| 1 or False | 1 |
	| 0 or False | False |
	| True and 1 | 1 |
	| True and 0 | 0 |
	| True or 1 | True |
	| True or 0 | True |
	| False and 1 | False |
	| False and 0 | False |
	| False or 1 | 1 |
	| False or 0 | 0 |

### 三大语句
* 顺序语句：自上而下执行语句

* 分支语句
	* if...
	* if...else...
	* if...elif...else...
	* 分支嵌套

* 循环结构
	* while
	* for...in...
	* for...in...else...，循环正常结束后执行else部分。
	* while...else...
	* break，终止循环的执行
	* continue，终止本轮循环的执行
	* range(m, n, s): 生成 m（默认为0） 到 n-1 的整数，整数间隔为 s（默认为1）。
	* 推导式的使用
	> ```python
	> list1 = [data for data in range(5)]
	> list1 = [data**2 for data in range(5)]
	> list1 = [data for data in range(5) if data > 2]
	> ```
