Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#symmetric difference update()
a={3,4,5,6,7,8,9,10,11,12}
b={4,5,6,7,8,9,10,11,12,13,14}
a.symmetric_diference_update(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.symmetric_diference_update(b)
AttributeError: 'set' object has no attribute 'symmetric_diference_update'. Did you mean: 'symmetric_difference_update'?
a.symmetric_difference_update(b)
a
{3, 13, 14}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#intersection update()
a={3,4,5,6,7,8,9,10,11}
b={4,5,6,7,8,9,10,11,12}
a.intersection_update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11}
b.intersection_update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11}
>>> a={2,3,4,5,6,7}
>>> b={1,2,3,4,5,6,8}
>>> a.copy()
{2, 3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> a={3,4,,5,6,7,8,9)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={3,4,5,6,7,8,9}
>>> a.pop()
3
>>> a
{4, 5, 6, 7, 8, 9}
>>> a.pop(4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(4)
>>> a
{5, 6, 7, 8, 9}
>>> #disjoint()
>>> a={2,3,4,5,6,7,8}
>>> b={7,8,9,10,11,13}
>>> a.isdisjoint(b)
False
>>> a={4,5,6,7,8}
>>> b={1,2,3,9,10}
>>> a.isdisjoint(b)
True
>>> len(a)
5
>>> a.count(4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
>>> a.discard(8)
>>> a
{4, 5, 6, 7}
