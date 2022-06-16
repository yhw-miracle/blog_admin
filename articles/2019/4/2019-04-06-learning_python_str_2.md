### 字符串的一些函数
* 划分函数
    * partition(self, *args, \*\*kwargs): Partition the string into three parts using the given separator. This will search for the separator in the string.  If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it. If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

    * rpartition(self, *args, \*\*kwargs): Partition the string into three parts using the given separator. This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it. If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

    * split(self, *args, \*\*kwargs): Return a list of the words in the string, using sep as the delimiter string. sep: The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit: Maximum number of splits to do. -1 (the default value) means no limit.

    * rsplit(self, *args, \*\*kwargs): Return a list of the words in the string, using sep as the delimiter string. sep: The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit: Maximum number of splits to do. -1 (the default value) means no limit. Splits are done starting at the end of the string and working to the front.

    * splitlines(self, *args, \*\*kwargs): Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

    > * 翻译
    > * partition(self, *args, \*\*kwargs): 从字符串左侧开始，根据指定参数将字符串划分为三部分，参数左侧、参数和参数右侧，组成三元元组并返回。如果指定参数不存在，三元元组由两个空项和自身组成。
    > * rpartition(self, *args, \*\*kwargs): 从字符串右侧开始，根据指定参数将字符串划分为三部分，参数左侧、参数和参数右侧，组成三元元组并返回。如果指定参数不存在，三元元组由两个空项和自身组成。
    > * split(self, *args, \*\*kwargs): 用指定参数作为分隔符将原字符串划分为若干字符串，组成列表返回。
    > * rsplit(self, *args, \*\*kwargs): 用指定参数作为分隔符将原字符串从右侧开始划分为若干字符串，组成列表返回。
    > * splitlines(self, *args, \*\*kwargs): 用分行符作为分隔符将原字符串划分若干个字符串，组成列表返回，其中分行符不会包括在结果字符串中。

    <hr />

 * 替换函数
    * replace(self, *args, \*\*kwargs): Return a copy with all occurrences of substring old replaced by new. count: Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences. If the optional argument count is given, only the first count occurrences are replaced.
    * expandtabs(self, *args, \*\*kwargs): Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

    > * 翻译
    > * replace(self, *args, \*\*kwargs): 使用新字符串替换原字符串中指定的字符串。
    > * expandtabs(self, *args, \*\*kwargs): 返回用空格替换字符串中的制表位的拷贝。

    <hr />

* 字符转换函数
    * lower(self, *args, \*\*kwargs): Return a copy of the string converted to lowercase.
    * upper(self, *args, \*\*kwargs): Return a copy of the string converted to uppercase.

    * swapcase(self, *args, \*\*kwargs): Convert uppercase characters to lowercase and lowercase characters to uppercase. 

    * title(self, *args, \*\*kwargs): Return a version of the string where each word is titlecased. More specifically, words start with uppercased characters and all remaining cased characters have lower case.

    * capitalize(self, *args, 、\*\*kwargs): Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.

    * casefold(self, *args, \*\*kwargs): Return a version of the string suitable for caseless comparisons.

    * startswith(self, prefix, start=None, end=None): S.startswith(prefix[, start[, end]]) -> bool   Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

    * endswith(self, suffix, start=None, end=None): S.endswith(suffix[, start[, end]]) -> bool   Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

    > * 翻译
    > * lower(self, *args, \*\*kwargs): 返回字符串中各字符转换为小写字符的拷贝。
    > * upper(self, *args, \*\*kwargs): 返回字符串中各个字符转换为大写的拷贝。
    > * swapcase(self, *args, \*\*kwargs): 将字符串的大写字符转换为小写字符，小写字符转换为大写字符。
    > * title(self, *args, \*\*kwargs): 返回首字母大写，其他小写的字符串。
    > * capitalize(self, *args, 、\*\*kwargs): 返回字符串首字母大写，其他小写。
    > * casefold(self, *args, \*\*kwargs): 返回字符串中所有字母转换为小写字母。

    > * startswith(self, prefix, start=None, end=None): 如果字符串以给定字符参数`prefix`开头，返回`True`；否则，返回`False`。如果给定`start`和`end`参数，则从`start`和`end`的位置进行检测。
    > * endswith(self, suffix, start=None, end=None): 如果字符串以给定字符参数`suffix`结尾，返回`True`；否则，返回`False`。如果给定`start`和`end`参数，则从`start`和`end`的位置进行检测。

    <hr />

* 其他函数
    * format(self, *args, \*\*kwargs): S.format(*args, \*\*kwargs) -> str   Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

    * format_map(self, mapping): S.format_map(mapping) -> str   Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces ('{' and '}').

    * count(self, sub, start=None, end=None): S.count(sub[, start[, end]]) -> int   Return the number of non-overlapping occurrences of substring sub in string S[start:end].  Optional arguments start and end are interpreted as in slice notation.

    * encode(self, *args, \*\*kwargs): Encode the string using the codec registered for encoding.   encoding: The encoding in which to encode the string.   errors: The error handling scheme to use for encoding errors. The default is 'strict' meaning that encoding errors raise a UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

    * join(self, ab=None, pq=None, rs=None): Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string. `Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'`

    * maketrans(self, *args, \*\*kwargs): Return a translation table usable for str.translate(). If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

    * translate(self, *args, \*\*kwargs): Replace each character in the string using the given translation table.table: Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None. The table must implement lookup/indexing via \_\_getitem\_\_, for instance a dictionary or list.  If this operation raises LookupError, the character is left untouched.  Characters mapped to None are deleted.

    > * 翻译
    > * format(self, *args, \*\*kwargs): 使用元组数据格式化字符串。
    > * format_map(self, mapping): 使用字典类型数据格式化字符串。
    > * count(self, sub, start=None, end=None): 返回指定的字符串在原字符串中出现的次数。如果给定`start`和`end`参数，则从`start`和`end`的位置进行检测。
    > * encode(self, *args, \*\*kwargs): 使用指定的编码方式给字符串编码。
    > * join(self, ab=None, pq=None, rs=None): 连接字符串，返回新的字符串。
    > * maketrans(self, *args, \*\*kwargs): 返回函数`tranlate()`需要的翻译表。一般是`maketrans(str1, str2)`。
    > * translate(self, *args, \*\*kwargs): 用给定的翻译表替换字符串中的每一个字符。一般是`translate(dict)`。
