由于第一次学习python，重新学习了一些语法知识

# Python 基础语法
## 1. Python 标识符
1. 标识符由字母、数字、下划线组成，不能以数字开头，区分大小写
2. 以下划线开头的标识符是有特殊意义
- 单下划线开头 _foo：
  - 代表不能直接访问的类属性，
  - 需通过类提供的接口进行访问，
  - 不能用 from xxx import * 而导入。
- 双下划线开头的 _ _foo
    - 代表类的私有成员
- 以双下划线开头和结尾的 \_ \_foo\_ \_
    - 代表 Python 里特殊方法专用的标识
    -  \_ \_init \_ \_() 代表类的构造函数。

## 2. Python 保留字符
1. 保留字不能用作常数或变数，或任何其他标识符名称。
2. 所有 Python 的关键字只包含小写字母。

and	exec	not
assert	finally	or
break	for	pass
class	from	print
continue	global	raise
def	if	return
del	import	try
elif	in	while
else	is	with
except	lambda	yield

and | exec | not
---|---|---
assert | finally |or
break |	for | pass
class  |	from    |	print
continue    |	global  |	raise
def |	if  |	return
del |	import  |	try
elif    |	in  |	while
else    |	is  |	with
except  |	lambda  |	yield

## 3. 行和缩进
1. Python 的代码块不使用大括号 {} 来控制类、函数以及其他逻辑判断。
2. python 最具特色的就是用缩进来写模块。

## 4. 多行语句
1. 使用斜杠（ \）将一行的语句分为多行显示

```
total = item_one + \
        item_two + \
        item_three
```
2. 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

```
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```
## 5. Python 引号
1. Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串
2. 三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

```
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个
段落。
包含了多个语句"""
```
## 6. Python注释

1. python中单行注释采用 # 开头。

```
# 第一个注释
print ("Hello, Python!")  # 第二个注释
```

2. python 中多行注释使用三个单引号(''')或三个双引号(""")。

```
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```
## 7、Python空行
1、函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。

2、类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

3、空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

## 8、等待用户输入

```
raw_input("按下 enter 键退出，其他任意键显示...\n")
python3
input("按下 enter 键退出，其他任意键显示...\n")
```
## 9. 同一行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

## 10. print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,。

## 11. 多个语句构成代码组
1. 缩进相同的一组语句构成一个代码块，我们称之代码组。
2. 我们将首行及后面的代码组称为一个子句(clause)。
```
if expression :
   suite
elif expression :
   suite
else :
   suite
```
## 12. import 与 from...import
1. 将整个模块(somemodule)导入，格式为：

```
import somemodule
```
2. 从某个模块中导入某个函数,格式为：

```
from somemodule import somefunction
```

3. 从某个模块中导入多个函数,格式为：

```
from somemodule import firstfunc, secondfunc, thirdfunc
```

4. 将某个模块中的全部函数导入，格式为：

```
from somemodule import *
```

