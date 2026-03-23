Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=3
b=6
print(a+b)
9
print(a-b)
-3
print(a*b)
18
print(a//b)
0
print(a/b)
0.5
print(a**b)
729
print(a%b)
3
#assignment
a=4
b=8
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
12
a-=b
a
4
a*=b
a
32
a//=2
a
16
a/=2
a
8.0
a**=2
a
64.0
a%=2
a
0.0
a=3
b=6
a+=b
b
6
a-=b
b
6
a*=3
b
6
a//=3
b
6
a/=3
b
6
a**=3
b
6
a%=3
b
6
#comparision
a=4
b=9
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a=7
b=7
a==b
True
#logical
a=4
b=2
a<b and b>a
False
a<b and b<a
False
a>b and b<a
True
a>=b and b<=a
True
a!=b and a==b
False
a>b or a<b
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=5
if type(a) is int:
    print("true")

    
true
if type(a) is not int:
    print("true")

    
a=2.6
if type(a) is float:
    print("it is float")

    
it is float
a=3.9
if type(a) is float:
    print("true")

    
true
#membership
a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print(10)

    
10
if 20 in a:
    print(20)

    
if 20 not in a:
    print(20)

    
20
#bitwise
a=4
b=3
a&b
0
bin(4)
'0b100'
>>> bin(3)
'0b11'
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(7)
'0b111'
>>> bin(5)
'0b101'
>>> #|
>>> a=5
>>> b=9
>>> a|b
13
>>> a=3
>>> b=6
>>> a|b
7
>>> #^
>>> a=3
>>> b=6
>>> a^b
5
>>> a=2
>>> b=4
>>> a^b
6
>>> #<<
>>> a=4
>>> b=8
>>> a<<b
1024
>>> a=3
>>> a<<2
12
>>> a=3
>>> a>>2
0
>>> #>>
>>> a=3
>>> a>>2
0
>>> a=4
>>> a>>2
1
