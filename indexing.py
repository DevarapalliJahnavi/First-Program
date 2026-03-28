Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[5]
'a'
a[3]
'a'
a[0]
'v'
a[1]
'i'
a[2]
'j'
a[0]+a[1]+a[2+]
SyntaxError: invalid syntax
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]+a[4]+a[7]
'   '
a="time is very precious"
a=[0]
a[8]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a[8]
IndexError: list index out of range
a="time is very precious"
a[8]
'v'
a[9]
'e'
a[10]
'r'
a[11]
'y'
a[8]+a[9]+a[10]+a[11]
'very'
a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
a[0]+a[1]+a[2]+a[3]
'time'
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'vijayawada'
a="i am learning python course"
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[18]+a[19]+a[20]+a[21]+a[22]+a[23]
'on cou'
a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
'course'
a[14+a[15]+a16]+a[17]+a[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[14+a[15]+a16]+a[17]+a[18]+a[19]
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a="i love python"
a[-11]+a[-10]+a[-9]+a[-8]
'love'
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a="vizag ia a city of destiny"
a[-7]+a[-6]+a[5]+a[-4]+a[-3]+a[-2]+a[-1]
'de tiny'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
>>> a="work until you succeed"
>>> a[0:5]
'work '
>>> a[10:13]
' yo'
>>> a[10:14]
' you'
>>> a[5:10]
'until'
>>> a[15:22]
'succeed'
>>> a="simple is better than complex"
>>> a[17:21]
'than'
>>> a[22:29]
'complex'
>>> a[10:16]
'better'
>>> a[0:6]
'simple'
>>> a="codegnan it solutions"
>>> a[-9:-1]
'solution'
>>> a[-9:-0]
''
>>> a[-9:-1]
'solution'
>>> a[-12:-10]
'it'
>>> a[-21:-13]
'codegnan'
>>> a="beautiful is better than ugly"
>>> a[-4:]
'ugly'
>>> b[-16:-10]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    b[-16:-10]
NameError: name 'b' is not defined
>>> a[-16:-10]
'better'
>>> a[-29:-20]
'beautiful'
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
a[::1]
'data science'
a[::3]
'dacn'
a="cloud"
a="cloud computing"
a[::4]
'cdmi'
a[::2]
'codcmuig'
a[::6]
'cci'
a[5:]
' computing'
a[3:11]
'ud compu'
a[:9]
'cloud com'
#striding 2nd method
a="machine learning"
a[1:7:2]
'ahn'
a[2:12:4]
'cea'
a[3:15:6]
'he'
a[1:14:3]
'ai ai'
#negative
a="python course"
a[-1:-9:-2]
'ero '
a[-3:-12:-4]
'r t'
a="python course"
a[7:3:2]
''
a[-6:-5:-2]
''
a[::1]
'python course'
a[::-1]
'esruoc nohtyp'
