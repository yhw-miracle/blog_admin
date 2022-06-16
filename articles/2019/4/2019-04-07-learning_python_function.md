### 函数
* 函数是将具有独立给你的代码块组织成为一个整体，使其具有特殊功能的代码集。函数的作用主要是加强代码的复用性，提高程序编写的效率。

* 无参函数、有参函数、带返回值的函数。

```python
# def 函数名([参数]):
	# 函数体
	# [return ...]

# 调用格式 ---> [变量=]函数名([参数])
```

* 若函数没有返回值，使用变量接收时结果为`None`。

* 函数定义时规定的参数为形参，函数调用时使用的参数为实参，形参的作用域为函数定义开始到定义结束。

* 变量的作用域可划分为局部变量（整个函数内部）和全局变量（整个文件）。

* 局部变量可添加关键字`global`提升作用域。

* 定义函数时，在函数名下用一对`"""`进行文档注释。

* 默认参数是函数或方法定义时指定形参的值，位置在位置形参的后面，调用该函数或方法时可以不指定默认参数的值，也可以指定默认参数的值，指定多个默认参数的值需要从左到右依次赋值。

* 关键字参数是在调用函数或方法时为指定名称的形参赋值所对应的实参.关键字参数需要在位置参数后面；不能对同一形参多次赋值；既可以为位置参数赋值，也可以为默认参数赋值。通常使用关键字参数是解决默认参数选择性赋值的问题。

* 可变参数是函数或方法定义时用于接收多个实参的形参，接收的多个实参组装成元组对象，定义可变参数的格式是`*args`。可变参数只能定义一个，定义在位置参数的后面。可变参数定义在位置参数后面。

* 字典参数是在函数或方法定义时，用于接收若干组未定义直接使用的关键字参数（调用后，会组装成字典对象），对应的形参。其定义格式是`**kwargs`。字典参数只能定义一个。

* 形参定义的顺序：先位置参数，再可变参数，后默认参数，再后字典参数。 

* 匿名函数，也称`lambda`表达式。

```python
# 方式一：
# 函数名 = lambda [形参] : 返回值
# 结果 = 函数名([实参])

# 方式二：
# 结果 = (lambda [形参] : 返回值)([实参])
```