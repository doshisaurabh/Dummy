Microsoft Windows [Version 10.0.26200.8037]
(c) Microsoft Corporation. All rights reserved.

C:\Users\SaurabhGauri>python
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> dict1 = {1:'Satish',2:'Dipak','ABC':'Saurabh'}
>>> dict1
{1: 'Satish', 2: 'Dipak', 'ABC': 'Saurabh'}
>>> dict1[99]
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    dict1[99]
    ~~~~~^^^^
KeyError: 99
>>> dict1[1]
'Satish'
>>> dict1['ABC']
'Saurabh'
>>> dict1['abc']
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    dict1['abc']
    ~~~~~^^^^^^^
KeyError: 'abc'
>>> dict.getdata()
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    dict.getdata()
    ^^^^^^^^^^^^
AttributeError: type object 'dict' has no attribute 'getdata'
>>> dict1.get()
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    dict1.get()
    ~~~~~~~~~^^
TypeError: get expected at least 1 argument, got 0
>>> dict1.get(1)
'Satish'
>>> dict1.get(99)
>>> dict1.get(99,'No Record')
'No Record'
>>> dict1.get(99,'No Record')
'No Record'
>>> dict2 = {1:'ABC', 2:'XYZ', 1:'Satish', 99:'Dipak'}
>>> dict2
{1: 'Satish', 2: 'XYZ', 99: 'Dipak'}
>>> dict2.pop(2)
'XYZ'
>>> dict2
{1: 'Satish', 99: 'Dipak'}
>>> dict2.append(44:'xyz')
  File "<python-input-16>", line 1
    dict2.append(44:'xyz')
                   ^
SyntaxError: invalid syntax
>>> dict2.append(44)
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    dict2.append(44)
    ^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'append'
>>> dict2.insert(44)
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    dict2.insert(44)
    ^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'insert'
>>>