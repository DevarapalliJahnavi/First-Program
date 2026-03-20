Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes conversions
>>> #int
>>> int(8)
8
>>> int(2.6)
2
>>> int("Indu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Indu")
ValueError: invalid literal for int() with base 10: 'Indu'
>>> int(2+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(2+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(2)
2.0
>>> float(8.9)
8.9
>>> float("hi")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
>>> float(3+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #string
>>> str(2)
'2'
>>> str(4.6)
'4.6'
>>> str("Indu")
'Indu'
str(4+2j)
'(4+2j)'
str(True)
'True'
str(False)
'False'
#complex
complex(6)
(6+0j)
complex(7.8)
(7.8+0j)
complex("c")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("c")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
complex(2+6j)
(2+6j)
#boolean
bool(2)
True
bool(4.6)
True
bool("Indu")
True
bool(2+4j)
True
bool(True)
True
bool(False)
False
