Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a=[4,6.7,"indu",5+9j,True,False]
>>> print(a)
[4, 6.7, 'indu', (5+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=60
>>> type(b)
<class 'int'>
>>> type(c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> c=[60]
>>> type(c)
<class 'list'>
>>> a=["python","java","c","c++"]
>>> a.append("html")
>>> a
['python', 'java', 'c', 'c++', 'html']
>>> a.append("css","js")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("css","js")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["css","js"])
>>> a
['python', 'java', 'c', 'c++', 'html', ['css', 'js']]
>>> #extend()
>>> a=["apple","banana","grapes"]
>>> a.extend(["mango","kiwi"])
>>> print(a)
['apple', 'banana', 'grapes', 'mango', 'kiwi']
>>> a.insert(1,"berry")
>>> a
['apple', 'berry', 'banana', 'grapes', 'mango', 'kiwi']
>>> a.index("grapes")
3
>>> a=["black","white","red"]
>>> \
...   a.sort()
SyntaxError: unexpected indent
>>> a.sort()
>>> a
['black', 'red', 'white']
b=["hyd","bng","vja"]
b.sort()
b
['bng', 'hyd', 'vja']
c=[7,9,2,0,3,5,100,28]
c.sort()
c
[0, 2, 3, 5, 7, 9, 28, 100]
a=["c","ds","ml","ai"]
a.reverse()
a
['ai', 'ml', 'ds', 'c']
b=[10,40,60,80]
b.reverse()
b
[80, 60, 40, 10]
c=[112,20,45,63,6,24]
c.reverse()
c
[24, 6, 63, 45, 20, 112]
a=["html","css","js","bs"]
a.pop()
'bs'
a
['html', 'css', 'js']
a.pop("js")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.pop("js")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'js'
a
['html', 'css']
a.remove("css")
a
['html']
a=["code","course","codegnan"]
a.clear()
a
[]
b=[]
a.append("indu")
b
[]
b=[]
b.append("indu")
b
['indu']
a=["hi","hello","how"]
a.copy()
['hi', 'hello', 'how']
b=a.copy()
b
['hi', 'hello', 'how']
c="hello"
len(c)
5
d=["hello"]
len(d)
1
a.count("how")
1
