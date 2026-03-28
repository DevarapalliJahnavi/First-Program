Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
a.count("i")
3
#find a string
a="code"
a.find("d")
2
a.find("e")
3
a.find("c")
0
#escape sequences
#\n-->new line
#\-->tab space
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
b="name:Indumathi\nmobileno:8247351529\tmailid:jahnavi.indumathi2409@gmail.com\ncity:vijayawada"
print(b)
name:Indumathi
mobileno:8247351529	mailid:jahnavi.indumathi2409@gmail.com
city:vijayawada
c="name\nmobileno\tmailid\ncity
SyntaxError: unterminated string literal (detected at line 1)
c="name\nmobileno\tmaildid\ncity\nid"
print(c)
name
mobileno	maildid
city
id
d="name:Indu\nmobileno:123456786789\tmaildid:sdfghj@gmail.com\ncity:vij\nid:1212"
print(d)
name:Indu
mobileno:123456786789	maildid:sdfghj@gmail.com
city:vij
id:1212
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait"."work",1)
SyntaxError: invalid syntax
b.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
#lower()
b="hi"
b.lower()
'hi'
b="HI"
b.lower()
'hi'
c="python"
c.upper()
'PYTHON'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'
a="python"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
a.startswith("p")
True
a.endswith("n")
True
b="python course"
b.isalpha()
False
c=234567
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="2345678"
c.isdigit()
True
a="Indumathi"
a.isalnum()
True
b="indu2406"
b.isalnum()
True
c="indu@2246"
c.isalnum()
False
#strip()
#lstrip(),rstrip()
a="    Indu    "
a.strip()
'Indu'
a.rstrip()
'    Indu'
a.lstrip()
'Indu    '
b="     meghana     "
a.strip()
'Indu'
b.strip()
'meghana'
b.rstrip()
'     meghana'
b.lstrip()
'meghana     '
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python course"
b.split()
['i', 'am', 'learning', 'python', 'course']
#join()
a="html","css","js","bs"
"".join(a)
'htmlcssjsbs'
" ".join(a)
'html css js bs'
"k".join(a)
'htmlkcsskjskbs'
b="indu","meghana"
" ".join(b)
'indu meghana'
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="indu"
lname="d"
print(fname+lname)
indud
print(fname+" "+lname)
indu d
print(fname.title()+" "+lname.title())
Indu D
print((fname+" "+lname).title())
Indu D
#formatting
a=6
b=8
print(a+b)
14
>>> print("the sum is",a+b)
the sum is 14
>>> print("the sum is a+b")
the sum is a+b
>>> name="Indu"
>>> print("the name is",name)
the name is Indu
>>> city="vij"
>>> print("the city is",city)
the city is vij
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello{}{}".format(a,b))
hellomotupatlu
>>> print("hello  {}  {}".format(a,b))
hello  motu  patlu
>>> print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> print("hello {}\n hello {}".format(a,b))
hello motu
 hello patlu
>>> #fstring
...  
>>> a="chota"
>>> b="bheem"
>>> print("hello {a}{b}")
hello {a}{b}
>>> print(f"hello {a}{b}")
hello chotabheem
>>> print(f"hello {a} hello {b}")
hello chota hello bheem
>>> a=5
>>> b=3
>>> print(a*b)
15
>>> c=a*b
>>> print("product is {}".format(c))
product is 15
>>> print(f"product is {c}")
product is 15
>>> print("product is {}".format(a*b))
product is 15
>>> print(f"product is {a*b}")
product is 15
