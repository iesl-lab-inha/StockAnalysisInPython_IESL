Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 3
>>> type(i)
<class 'int'>
>>> 
>>> f = 1.0
>>> type(f)
<class 'float'>
>>> var = i * f
>>> print('{} : {}'.format(var, type(var)))
3.0 : <class 'float'>
>>> googol = 10 ** 100
>>> type(googol)
<class 'int'>
>>> googol
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> s = 'string'
>>> type(s)
<class 'str'>
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> def getCAGR(first, last, years):
	return (last/firtst)**(1/years) - 1

>>> cagr = getCAGR(65300, 2669000, 20)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cagr = getCAGR(65300, 2669000, 20)
  File "<pyshell#16>", line 2, in getCAGR
    return (last/firtst)**(1/years) - 1
NameError: name 'firtst' is not defined
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> def getCAGR(first, last, years):
	return (last/first)**(1/years) - 1

>>> cagr = getCAGR(65300, 2669000, 20)
>>> print("SEC CAGR : {:.2%}".format(cagr))
SEC CAGR : 20.38%
>>> 