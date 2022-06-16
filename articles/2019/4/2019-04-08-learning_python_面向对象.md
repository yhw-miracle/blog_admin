### 面向对象
#### 类和对象
* 类是一系列事物的统称，包括成员变量和成员方法，统称类成员。

* 类的关键字是class，命名满足大驼峰命名法。

* 对象是类的实例，self仅出现在成员方法中，指代执行该方法的对象。

* 类在__init__(self)方法中创建对象时初始化公有成员变量；对象可以声明独有变量；类可以定义属于类的类变量，类变量可以私有化。

* 类的方法有成员方法、类方法、私有方法和静态方法。

```python
class AAA:
	def bbb(self[,args]):
		'''成员方法'''
		'''实例变量，实例方法，类变量，类方法均可使用'''
		pass
```
___
```python
class AAA:
	@classmethod
	def bbb(cls[,args]):
	'''类方法'''
	'''不能使用实例变量和实例方法'''
	'''可以使用类变量和类变量'''
	pass
```
___
```python
class AAA:
	def __bb(self[,args]):
	'''私有方法'''
	'''只能在类的内部使用'''
	pass
```
___
```python
class AAA:
	@staticmethod
	def bbb([args]):
	'''静态方法'''
	'''一般不访问成员变量和类变量'''
	pass
```

| 成员方法 | 适用范围 |
| ------ | ------ |
| 成员方法 | 只访问成员变量 |
| 类方法 | 只访问类变量 |
| 成员方法 | 既访问成员变量，又访问类变量 |
| 静态方法 | 既不访问成员变量，又不访问类变量 |

* 魔术方法
    * __init__(self)，创建对象时初始化公有成员变量。
    * __str__(self)，打印对象时自动调用的方法。
  * __new__(cls, *args, **kwargs)，创建对象时自动执行（创建对象由object类的__new__方法执行）。
    * __del__(self)，销毁对象时自动执行。

* ==与is的区别：==判断的是内容，is判断的是地址。

* 单例设计模式

```python
class AAA:
    # 单例设计模式
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(AAA)
        return cls.__instance
```

#### 封装
* 封装是对类成员进行访问控制，保护数据不被非法访问。

* 一般对成员变量进行封装，需要给出访问接口。

```python
class AAA:
	self.__bbb = 1
	def get_bbb(self):
		return self.__bbb
	def set_bbb(self):
		self.__bbb = 2
```

#### 继承
* 子类可以使用父类的成员变量、类变量、成员方法、类方法、静态方法。子类不能使用父类的私有方法。

* 获取继承关系的属性__mro__。

* 重写：子类重新定义与父类相同的成员方法。

* 子类中访问父类被重写的方法

```python
# 1. 父类名.方法名(对象)
# 2. super(本类名, 对象).方法名()
# 3. super().方法名()
```

* python支持多继承，访问父类成员时遇到冲突，访问继承的第一个父类的成员。

#### 多态
* 父类的引用指向子类对象。不同子类调用相同的父类方法，执行结果不同。

* 鸭子类型，类与类之间不用共同继承一个父类，只需要将它们做得像一种事物即可。

> Duck typing 这个概念来源于美国印第安纳州的诗人詹姆斯·惠特科姆·莱利（James Whitcomb Riley,1849- 1916）的诗句：”When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.” 
