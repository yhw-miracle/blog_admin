### 元组
* 元组（tuple）（`()`）是一种存储固定数据的存储模型，元组中的数据通过索引修改。

* 元组中的数据若是非引用类型数据，不允许修改；若是引用类型数据，不允许修改对象，可以修对象的值。

* 元组函数
    * count(self, x): Return number of occurrences of value.
    * index(self, x, start, end): Return first index of value.Raises ValueError if the value is not present
    > * 翻译
    > * count(self, x): 返回元组中指定数据出现的次数。
    > * index(self, x, start, end): 返回指定数据在元组中出现的第一个位置，若指定数据不存在，抛出ValueError。

### 集合
* 集合（set）（`{,,...}`）是一种存储无序不重复数据的存储模型，没有索引概念。

* 集合中的函数
    * add(self, element): Add an element to a set.This has no effect if the element is already present.
    * clear(self): Remove all elements from this set.
    * copy(self): Return a shallow copy of a set.
    * pop(self): Remove and return an arbitrary set element.Raises KeyError if the set is empty.
    * remove(self ,element): Remove an element from a set; it must be a member.If the element is not a member, raise a KeyError.
    > * 翻译
    > * add(self, element): 添加一个元素到集合中，若改元素已经存在，集合将无任何影
    > * clear(self): 移除集合中所有元素。
    > * copy(self): 返回集合的拷贝体。
    > * pop(self): 移除并返回这个该集合中随意一个元素，若集合为空，抛出KeyError
    > * remove(self ,element): 移除集合中指定的元素，若指定元素不存在，抛出KeyError

    <hr />

    * isdisjoint(self, s): Return True if two sets have a null intersection.
    * issubset(self ,s): Report whether another set contains this set.
    * issuperset(self, s): Report whether this set contains another set.
    > * 翻译
    > * isdisjoint(self, s): 若两个集合没有交集，返回True。
    > * issubset(self ,s): 报告另一个集合是否包含该集合，若包含，返回True；若不包含，返回False。
    > * issuperset(self, s): 报告这个集合是否包含另一个集合，若包含，返回True；若不包含，返回False。

    <hr />

    * difference(self, s): Return the difference of two or more sets as a new set.(i.e. all elements that are in this set but not the others.)
    * difference_update(self,  s): Remove all elements of another set from this set.
    * discard(self, element): Remove an element from a set if it is a member.If the element is not a member, do nothing.
    > * 翻译
    > * difference(self, s): 记录该集合与其他集合之间的不同元素，组成新的集合并返回（简单来说，返回集合中的所有元素在该集合中，不在其他集合中）。
    > * difference_update(self,  s): 移除另一个集合中与该集合相同的元素。
    > * discard(self, element): 移除集合中的指定元素，若该元素不存，则不做任何事。

    <hr />

    * intersection(self, s): Return the intersection of two sets as a new set.(i.e. all elements that are in both sets.)
    * intersection_update(self,  s): Update a set with the intersection of itself and another.
    > * 翻译
    > * intersection(self, s): 记录两个集合的交集，组成新的集合并返回（简单来说，新的集合中元素是两个集合中都有的元素）。
    > * intersection_update(self,  s): 将该集合和另一个集合的交集更新到该集合中。

    <hr />

    * symmetric_difference(self,  s): Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
    * symmetric_difference_update(self,  s): Update a set with the symmetric difference of itself and another.
    * union(self, s): Return the union of sets as a new set.(i.e. all elements that are in either set.)
    * update(self,  s): Update a set with the union of itself and others.
    > * 翻译
    > * symmetric_difference(self,  s): 记录两个集合的均匀区别，组成新的集合并返回（简单来说，新的集合中元素只存在于其中一个集合中）。
    > * symmetric_difference_update(self,  s): 将两个集合的均匀区别更新到该集合中。
    > * union(self, s): 记录两个集合之间的并集，组成新的集合并返回（简单来说，两个集合中所有元素）。
    > * update(self,  s): 将两个集合之间的并集更新到该集合中。
