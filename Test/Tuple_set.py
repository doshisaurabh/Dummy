Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
tup = [1,567,798,265,3465,47]
tup
[1, 567, 798, 265, 3465, 47]
tupa = [766,8,83,90856,4u69]
SyntaxError: invalid decimal literal
tupa = [766,8,83,90856,'4u69']
tupa = 766,8,83,90856,'4u69'
tupa
(766, 8, 83, 90856, '4u69')
tupa.count(8)
1
tupa[0]=123
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tupa[0]=123
TypeError: 'tuple' object does not support item assignment
tupb=123,67325,[3675,7786,678],'ssdfjs'
tuuba
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuuba
NameError: name 'tuuba' is not defined. Did you mean: 'tupa'?
tuba
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tuba
NameError: name 'tuba' is not defined. Did you mean: 'tupa'?
tupb
(123, 67325, [3675, 7786, 678], 'ssdfjs')
tupb[2:1]=675
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tupb[2:1]=675
TypeError: 'tuple' object does not support item assignment
tupb[2][1]=675
tupb
(123, 67325, [3675, 675, 678], 'ssdfjs')
4



tubb
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tubb
NameError: name 'tubb' is not defined. Did you mean: 'tupb'?
tupb
(123, 67325, [3675, 675, 678], 'ssdfjs')
123 in tupb
True
'4u' in tup
False
False
False



clear
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
cls
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
set1={1,2,56,678,43,1,25}
set1
{1, 2, 678, 56, 25, 43}
type(set1)
<class 'set'>
set2 = {1,'abc','sabhj',15.2876}
set2
{1, 15.2876, 'abc', 'sabhj'}
set1 + set2
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    set1 + set2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
set1 - set2
{2, 678, 43, 56, 25}
set1 | set2
{1, 2, 678, 'abc', 'sabhj', 43, 15.2876, 56, 25}
set1 ^ set2
{2, 'abc', 'sabhj', 678, 43, 15.2876, 56, 25}
set2 ^ set2
set()
set2 - set2
set()
set2 - set1
{'sabhj', 'abc', 15.2876}
