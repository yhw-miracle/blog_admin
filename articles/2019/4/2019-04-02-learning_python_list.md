### 数据结构
* python 中的数据结构
    * 不可变类型
        * int：整型
        * float：浮点型
        * bool：布尔型
        * str：字符串
    * 可变类型
        * list：列表
        * tuple：元组
        * set：集合
        * dict：字典

* 获取数据类型：`type()`
> 如：
> ```ipython
> In [1]: type(1)
> Out[1]: int
> In [2]: type(1.1)
> Out[2]: float
> In [3]: type(True)
> Out[3]: bool
> In [3]: type(False)
> Out[3]: bool 
> ```

### 列表
* 列表（list）（`[]`）是一种存储大量数据的存储模型，可以对数据进行增、删、改、查操作。
* 增加数据
    * append(self, object): Append object to the end of the list.
    * insert(self, index, object): Insert object before index.
    * extend(self, iterable): Extend list by appending elements from the iterable.
    > * 翻译：
    > * append(self, object): 在列表的末尾添加元素。
    > * insert(self, index, object): 在指定位置之前插入元素。
    > * extend(self, iterable): 从可迭代数据存储器中扩充到列表末尾。

* 删除数据
    * remove(self, object): Remove first occurrence of value.Raises ValueError if the value is not present.
    * pop(self, index): Remove and return item at index (default last).Raises IndexError  if list is empty or index is out of range.
    * clear(self): Remove all items from list.
    > * 翻译：
    > * remove(self, object): 移除列表中第一个指定数据，若指定数据不存在，抛出ValueError。
    > * pop(self, index): 移除并返回列表中指定位置的数据（默认为最后一个），若列表为空或者指定位置超过范围，抛出IndexError。
    > * clear(self): 移除列表中所有元素。

* 修改数据和查询数据：**根据索引**

* 其他函数
    * count(self, object): Return number of occurrences of value.
    * index(self, object, start, stop): Return first index of value.Raises ValueError if the value is not present.
    * copy(self): Return a shallow copy of the list.
    * reverse(self): Reverse *IN PLACE*.
    * sort(self, key, reverse): Stable sort *IN PLACE*.
    > * 翻译
    > * count(self, object): 返回指定数据在列表中的个数。
    > * index(self, object, start, stop): 返回指定数据在列表中第一个位置，若指定数据不存在，抛出ValueError。
    > * copy(self): 返回一个列表的拷贝。
    > * reverse(self): 在列表上反转。
    > * sort(self, key, reverse): 在列表上执行稳定排序。
