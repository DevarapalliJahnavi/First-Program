Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"indu","year":2026,"month":3}
print(a)
{'name': 'indu', 'year': 2026, 'month': 3}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['indu', 2026, 3])
a.items()
dict_items([('name', 'indu'), ('year', 2026), ('month', 3)])
#update
a={"name":"indu","city":"vja","date":31}
a.update({"year":2026})
a
{'name': 'indu', 'city': 'vja', 'date': 31, 'year': 2026}
a.update({"month":3},{"time":10})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"month":3},{"time":10})
TypeError: update expected at most 1 argument, got 2
a.update({"month":3,"time":10})
a
{'name': 'indu', 'city': 'vja', 'date': 31, 'year': 2026, 'month': 3, 'time': 10}
#setdefault
a={"mailid":"jahnavi.indumathi2409@gmail.com"}
a.setdefault("name","indu")
'indu'
a
{'mailid': 'jahnavi.indumathi2409@gmail.com', 'name': 'indu'}
a.pop()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("name")
'indu'
a
{'mailid': 'jahnavi.indumathi2409@gmail.com'}
a.pop("jahnavi.indumathi2409@gmail.com")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop("jahnavi.indumathi2409@gmail.com")
KeyError: 'jahnavi.indumathi2409@gmail.com'
>>> a.copy()
{'mailid': 'jahnavi.indumathi2409@gmail.com'}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"day":"tuesday"})
>>> b
{'day': 'tuesday'}
>>> #get
>>> a={"cit":"vja","country":"india"}
>>> a.get("country")
'india'
>>> a
{'cit': 'vja', 'country': 'india'}
>>> a["cit"]
'vja'
>>> a
{'cit': 'vja', 'country': 'india'}
>>> a.popitem()
('country', 'india')
>>> a
{'cit': 'vja'}
>>> a={"idnos":[10,20,30],"names":["indu","meghana","sowjanya"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['indu', 'meghana', 'sowjanya']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['indu', 'meghana', 'sowjanya']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['indu', 'meghana', 'sowjanya'])])
>>> a={"name":"indu","city":"vja","name":"indu"}
>>> print(a)
{'name': 'indu', 'city': 'vja'}
>>> a={"name":"indu","city":"vja","name":"indumathi"}
>>> print(a)
{'name': 'indumathi', 'city': 'vja'}
>>> a={"name":"indu","city":"vja","name1":"indu"}
>>> print(a)
{'name': 'indu', 'city': 'vja', 'name1': 'indu'}
