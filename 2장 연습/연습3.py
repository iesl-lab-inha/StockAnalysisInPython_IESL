Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics'}
>>> crispr[1]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    crispr[1]
KeyError: 1
>>> crispr['NTLA']
'Intellia Therapeutics'
>>> crispr['CRSP'] = 'CRISPER Therapeutics'
>>> crispr
{'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics', 'CRSP': 'CRISPER Therapeutics'}
>>> len(crispr)
3
>>> for x in crispr
SyntaxError: invalid syntax
>>> for x in crispr:
	print('%s : %s' % (x, crispr[x]))

	
EDIT : Editas Medicine
NTLA : Intellia Therapeutics
CRSP : CRISPER Therapeutics
>>> for x in crispr:
	print('{} : {}'.format(x, crispr[x]))


EDIT : Editas Medicine
NTLA : Intellia Therapeutics
CRSP : CRISPER Therapeutics
>>>  for x in crispr:
	print(f'{x} : {crispr[x]}')
	
SyntaxError: unexpected indent
>>> for x in crispr:
	print(f'{x} : {crispr[x]}')

	
EDIT : Editas Medicine
NTLA : Intellia Therapeutics
CRSP : CRISPER Therapeutics
>>> 
================================ RESTART: Shell ================================
>>> s = {'A', 'P', 'P', 'L', 'E'}
>>> s
{'A', 'P', 'E', 'L'}
>>> mySet = {'B', 6, 1, 2}
>>> mySet
{1, 2, 6, 'B'}
>>> if 'B' in mySet:
	print("'B' exists in", mySet)

	
'B' exists in {1, 2, 6, 'B'}
>>> setA = {1, 2, 3, 4, 5}
>>> setB = {3, 4, 5, 6, 7}
>>> 
>>> setA & setB
{3, 4, 5}
>>> setA | setB
{1, 2, 3, 4, 5, 6, 7}
>>> setA - setB
{1, 2}
>>> setB - setA
{6, 7}
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> ls = []
>>> d = {}
>>> t = ()
>>> s = set()
>>> ls = [1, 3, 5, 2, 2, 3, 4, 2, 1, 1, 1, 5]
>>> list(set(ls))
[1, 2, 3, 4, 5]
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> import timeit
>>> iteration_test = """
    for i in itr :
	pass
    """
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number = 1000)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    timeit.timeit(iteration_test, setup='itr = list(range(10000))', number = 1000)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 122, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 3
    for i in itr :
    ^
IndentationError: unexpected indent
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 122, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 3
    for i in itr :
    ^
IndentationError: unexpected indent
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> import timeit
>>> iteration_test = """
for i in itr :
pass
"""
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number = 1000)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    timeit.timeit(iteration_test, setup='itr = list(range(10000))', number = 1000)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 122, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 4
    pass
       ^
IndentationError: expected an indented block
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> import timeit
>>> iteration_test = """
    for i in itr :
	pass
    """
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\timeit.py", line 122, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 3
    for i in itr :
    ^
IndentationError: unexpected indent
>>> 