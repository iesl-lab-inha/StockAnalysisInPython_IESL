Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList = ['Thoughts', 'became', 'things.']
>>> newList = myList[:]
>>> newList
['Thoughts', 'became', 'things.']
>>> newList[-1] = 'actions.'
>>> newList
['Thoughts', 'became', 'actions.']
>>> myList
['Thoughts', 'became', 'things.']
>>> 
=============================== RESTART: Shell ===============================
>>> nums = [1, 2, 3, 4, 5]
>>> squares = []
>>> for x in nums:
	squares.append(x ** 2)

	
>>> squares
[1, 4, 9, 16, 25]
>>> 
=============================== RESTART: Shell ===============================
>>> nums = [1, 2, 3, 4, 5]
>>> squares = [x ** 2 for x in nums]
>>> squares
[1, 4, 9, 16, 25]
>>> 
=============================== RESTART: Shell ===============================
>>> nums = [1, 2, 3, 4, 5]
>>> even_squares = [x ** 2 for x in nums if x % 2 == 0]
>>> even_squares
[4, 16]
>>> 
=============================== RESTART: Shell ===============================
>>> myTuple = ('a', 'b', 'c', [10, 20, 30], abs, max)
>>> myTuple[3]
[10, 20, 30]
>>> myTuple[4](-100)
100
>>> myTuple[5](myTuple[3])
30
>>> myTuple[0] = 'A'

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    myTuple[0] = 'A'
TypeError: 'tuple' object does not support item assignment
>>> 
=============================== RESTART: Shell ===============================
>>> crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics'}
>>> crispr[1]

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    crispr[1]
KeyError: 1
>>> crispr['NTLA
       
SyntaxError: EOL while scanning string literal
>>> crispr['NTLA']
'Intellia Therapeutics'
>>> crispr['CRSP'] = 'CRISPER Therapeutics'
>>> crispr
{'EDIT': 'Editas Medicine', 'CRSP': 'CRISPER Therapeutics', 'NTLA': 'Intellia Therapeutics'}
>>> len(crispr)
3
>>> for x in crispr
SyntaxError: invalid syntax
>>> for x in crispr:
	print('%s : %s' % (x, crispr[x]))

	
EDIT : Editas Medicine
CRSP : CRISPER Therapeutics
NTLA : Intellia Therapeutics
>>> for x in crispr:
	print('{} : {}'.format(x, crispr[x]))

	
EDIT : Editas Medicine
CRSP : CRISPER Therapeutics
NTLA : Intellia Therapeutics
>>> for x in crispr:
	print(f'{x} : {crispr[x]}')
	
SyntaxError: invalid syntax
>>> for x in crispr:
	print('f{x} : {crispr[x]}')

	
f{x} : {crispr[x]}
f{x} : {crispr[x]}
f{x} : {crispr[x]}
>>> >>> for x in crispr:
	print(f'{x} : {crispr[x]}')
	
SyntaxError: invalid syntax
>>> for x in crispr:
	print(f'{x} : {crispr[x]}')


           

           
