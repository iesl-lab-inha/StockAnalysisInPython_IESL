Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> keyword.__file__
'C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python38\\lib\\keyword.py'
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> import calendar
>>> print (calendar.month(2022,7))
     July 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

>>> from calendar import month
>>> print (month(2022, 7))
     July 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> import datatime
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import datatime
ModuleNotFoundError: No module named 'datatime'
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> import datetime
>>> print(datetime.datetime.now())
2022-06-30 15:38:57.006243
>>> from datetime import datetime as dt
>>> print(dt.now())
2022-06-30 15:39:17.218117
>>> 
================================ RESTART: Shell ================================
>>> import urllib.request
>>> type(urllig.request)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type(urllig.request)
NameError: name 'urllig' is not defined
>>> 
================================ RESTART: Shell ================================
>>> import urllib.request
>>> type(urllib.request)
<class 'module'>
>>> 
================================ RESTART: Shell ================================
>>> import urllib
>>> type(urllib)
<class 'module'>
>>> urllib.__path__
['C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python38\\lib\\urllib']
>>> urllib.__package__
'urllib'
>>> 