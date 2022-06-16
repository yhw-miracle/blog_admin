### 异常处理
* 异常处理格式

```python
try:
	# 可能引发异常现象的代码
	pass
except:
	# 出现异常时执行的代码
	# 可有多个 except 代码块，但只执行一条 except 代码块
	# 一般格式：except 异常类名[ as 变量名]
	# 一般捕获异常类型从小到大
	# Exception 类是所有异常类的父类
	pass
else:
	# 未出现异常时执行的代码
	pass
finally:
	# try 代码块结束时执行的代码
	pass
```

* 异常抛出格式

```python
raise # 异常类对象
```

* 自定义异常

```python
class AAA(Exception):
	""" AAA 为自定义异常类名"""
	pass
```
