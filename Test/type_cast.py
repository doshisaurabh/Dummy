Microsoft Windows [Version 10.0.26200.8037]
(c) Microsoft Corporation. All rights reserved.

C:\Users\SaurabhGauri>python
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> int("str")
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    int("str")
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: 'str'
>>> int("5")
5
>>> int("10.5")
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    int("10.5")
    ~~~^^^^^^^^
ValueError: invalid literal for int() with base 10: '10.5'
>>> float("10.5")
10.5
>>> complex("10.5")
(10.5+0j)
>>> complex(10,20)
(10+20j)
>>> complex("10",20)
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    complex("10",20)
    ~~~~~~~^^^^^^^^^
TypeError: complex() argument 'real' must be a real number, not str
>>> complex("10","20")
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    complex("10","20")
    ~~~~~~~^^^^^^^^^^^
TypeError: complex() argument 'real' must be a real number, not str
>>> complex(10,"20")
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    complex(10,"20")
    ~~~~~~~^^^^^^^^^
TypeError: complex() argument 'imag' must be a real number, not str
>>> complex(10,20)
(10+20j)
>>> float(True)
1.0
>>> complex(False)
0j
>>> complex(True)
(1+0j)
>>> bool(5)
True
>>> bool(10+20j)
True
>>> bool(0+20j)
True
>>> bool(0+0j)
False
>>> bool("Saurabh")
True
>>> bool("False")
True
>>> bool("True")
True
>>> bool("No")
True
>>> bool(10.1215)
True
>>> bool(0.121)
True
>>> bool('')
False
>>>
>>> int(0B1111)
15
>>> int(0Xface)
64206
>>> float(0Xface)
64206.0
>>>