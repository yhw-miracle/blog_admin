### 字典
* 字典（dict）（`{xx: xx,...}`）是一种使用“键值对结构”存储数据的存储模型，没有索引概念，利用键（键是**唯一**的）来索引，可以根据键对字典数据进行增、删、改、查操作。

* 字典中的函数
    * clear(self):  D.clear() :  None.  Remove all items from D.
    * copy(self): D.copy() :  a shallow copy of D.
    * fromkeys(seq): Create a new dictionary with keys from iterable and values set to value.
    > * 翻译
    > * clear(self): 清空字典中的所有项。
    > * copy(self): 返回字典的一个拷贝。
    > * fromkeys(seq): 用来自迭代器作为键，值集合作为值，创建新的字典。

    <hr />

    * get(self, k): Return the value for key if key is in the dictionary, else default.
    * items(self): D.items() :  a set-like object providing a view on D's items.
    * keys(self): D.keys() :  a set-like object providing a view on D's keys.
    * values(self): D.values() :  an object providing a view on D's values.
    > * 翻译
    > * get(self, k): 返回指定的键对应的值。
    > * items(self): 获取字典中所有键值对，以列表形式返回。
    > * keys(self): 获取字典中所有键，以列表的形式返回。
    > * values(self): 获取字典中所有值，以列表的形式返回。

    <hr />

    * pop(self,  k): D.pop(k[,d]) :  v, remove specified key and return the corresponding value.If key is not found, d is returned if given, otherwise KeyError is raised.
    * popitem(self): D.popitem() :  (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.
    > * 翻译
    > * pop(self,  k[, d]): 移除字典中指定的键，并返回对应的值。如果指定的键不存在，若给出d，则返回d；否则将抛出KeyError。
    > * popitem(self): 移除字典中最后一对键值对，并以二元元组的形式返回。若字典为空，抛出KeyError。

    <hr />

    * setdefault(self, k,  default): Insert key with a value of default if key is not in the dictionary.Return the value for key if key is in the dictionary, else default.
    > * 翻译
    > * setdefault(self, k,  default): 如果指定的键不在字典中，将指定的键和值（没有，默认为None）插入到字典中，并返回值。

    <hr />

    * update(self, E=None, \*\*F): D.update([E, ]\*\*F) :  None.  Update D from dict/iterable E and F. If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]. If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v. In either case, this is followed by: for k in F:  D[k] = F[k].
    > * 翻译
    > * update(self, E=None, \*\*F): 使用新字典中的数据对原始字典数据进行更新。如果字典E存在，有keys()方法，则执行代码for k in E: D[k] = E[K]；如果迭代器E存在，缺失keys()方法，则执行代码for k, v in E: D[k] = v；如果字典或迭代器E不存在，则执行代码for k in F: D[k] = F[k]。

* 当需要存储大量数据，并且期望在编程期以最快速度获取单个数据，或者使用非对象格式保存单个对象的属性值，推荐选择字典来存储。
