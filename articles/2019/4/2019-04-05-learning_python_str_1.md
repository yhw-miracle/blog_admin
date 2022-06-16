### 字符串
* 字符串是一个包含若干个字符并按照一定顺序排列成整体的容器，支持`索引`操作，字符串定义可以是`"xxxx"`,`'xxx'`,`"""xxx"""`,`'''xxx'''`。

> 字符串的一些函数，函数较多，用分割线划分。

 * 判断函数
    * isalnum(self, *args, \*\*kwargs): Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

    * isalpha(self, *args, \*\*kwargs): Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

    * isascii(self, *args, \*\*kwargs): Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

    * isdecimal(self, *args, \*\*kwargs): Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

    * isdigit(self, *args, \*\*kwargs): Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are digits and there is at least one character in the string.

    * isidentifier(self, *args, \*\*kwargs): Return True if the string is a valid Python identifier, False otherwise. Use keyword.iskeyword() to test for reserved identifiers such as "def" and "class".

    * islower(self, *args, \*\*kwargs): Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

    * isnumeric(self, *args, \*\*kwargs): Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and there is at least one character in the string.

    * isprintable(self, *args, \*\*kwargs): Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in repr() or if it is empty.

    * isspace(self, *args, \*\*kwargs): Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

    * istitle(self, *args, \*\*kwargs): Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

    * isupper(self, *args, \*\*kwargs): Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

    > * 翻译
    > * isalpha(self, *args, \*\*kwargs): 判断字符串是否全是字母。
    > * isalnum(self, *args, \*\*kwargs): 判断字符串是否字母数字。
    > * isascii(self, *args, \*\*kwargs): 判断字符串是否全是`ASCII`字符。
    > * isdecimal(self, *args, \*\*kwargs): 判断字符串是否全是数字。
    > * isdigit(self, *args, \*\*kwargs): 判断字符串是否全是数字。
    > * isidentifier(self, *args, \*\*kwargs): 判断字符串是否是有效的`python`标识符。
    > * islower(self, *args, \*\*kwargs): 判断字符串是否全是小写。
    > * isnumeric(self, *args, \*\*kwargs): 判断字符串是否全是数字。
    > * isprintable(self, *args, \*\*kwargs): 判断字符串是否是可打印的。
    > * isspace(self, *args, \*\*kwargs): 判断字符串是否是空白字符。
    > * istitle(self, *args, \*\*kwargs): 判断字符串是否是首字母大写，其他小写。
    > * isupper(self, *args, \*\*kwargs): 判断字符串是否全是大写。

    <hr />

 * 格式转换函数
    * strip(self, *args, \*\*kwargs): Return a copy of the string with leading and trailing whitespace remove. If chars is given and not None, remove characters in chars instead.

    * lstrip(self, *args, \*\*kwargs): Return a copy of the string with leading whitespace removed. If chars is given and not None, remove characters in chars instead.

    * rstrip(self, *args, \*\*kwargs): Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

    * ljust(self, *args, \*\*kwargs): Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).

    * rjust(self, *args, \*\*kwargs): Return a right-justified string of length width. Padding is done using the specified fill character (default is a space).

    center(self, *args, \*\*kwargs): Return a centered string of length width. Padding is done using the specified fill character (default is a space).

    zfill(self, *args, \*\*kwargs): Pad a numeric string with zeros on the left, to fill a field of the given width.The string is never truncated.

    > * 翻译
    > * strip(self, *args, \*\*kwargs): 返回去掉字符串左右两侧空白字符或指定字符的拷贝。
    > * lstrip(self, *args, \*\*kwargs): 返回去掉字符串左侧空白字符或指定字符的拷贝。
    > * rstrip(self, *args, \*\*kwargs): 返回去掉字符串右侧空白字符或指定字符的拷贝。

    > * ljust(self, *args, \*\*kwargs): 返回右侧用空格或指定字符补齐指定宽度的字符串。
    > * rjust(self, *args, \*\*kwargs): 返回左侧用空格或指定字符补齐指定宽度的字符串。

    > * center(self, *args, \*\*kwargs): 填充字符串左右两侧几乎相等的指定字符或空格，是字符串居于中间位置，返回这样的字符串。

    > * zfill(self, *args, \*\*kwargs): 用`0`在数字字符串的左边补齐给定的宽度，字符串不会`truncated`。

    <hr />

* 查询函数
    * find(self, sub, start=None, end=None): S.find(sub[, start[, end]]) -> int   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

    * rfind(self, sub, start=None, end=None): S.rfind(sub[, start[, end]]) -> int   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

    * index(self, sub, start=None, end=None): S.index(sub[, start[, end]]) -> int   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

    * rindex(self, sub, start=None, end=None): S.rindex(sub[, start[, end]]) -> int   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

    > * 翻译
    > * find(self, sub, start=None, end=None): 返回指定字符串在原字符串中出现的最小下标。若给定`start`和`end`，则在指定范围里搜索；若指定字符串未发现，则返回`-1`。
    > * rfind(self, sub, start=None, end=None): 返回指定字符串在原字符串中出现的最大下标。若给定`start`和`end`，则在指定范围里搜索；若指定字符串未发现，则返回`-1`。
    > * index(self, sub, start=None, end=None): 返回指定字符串在原字符串中出现的最小下标。若给定`start`和`end`，则在指定范围里搜索；若指定字符串未发现，则抛出`ValueError`。
    > * rindex(self, sub, start=None, end=None): 返回指定字符串在原字符串中出现的最大下标。若给定`start`和`end`，则在指定范围里搜索；若指定字符串未发现，则抛出`ValueError`。
