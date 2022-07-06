Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> class MyFirstClass:
	clasVar = 'The best way to predict the futuer is to invent it.'
	def clsMethod(self):
		print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

		
>>> mfc = MyFirstClass()
>>> mfc.clsVar
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mfc.clsVar
AttributeError: 'MyFirstClass' object has no attribute 'clsVar'
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> class MyFirstClass:
	clsVar = 'The best way to predict the futuer is to invent it.'
	def clsMethod(self):
		print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

		
>>> mfc = MyFirstClass()
>>> mfc.clsVar
'The best way to predict the futuer is to invent it.'
>>> mfc.clsMethod()
The best way to predict the futuer is to invent it.	- Alan Curtis Kay -
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> class A:
	def methodA(self):
		print("Calling A's methodA")
	def method(self):
		print("Calling A's method")

		
>>> class B:
	def methodB(self):
		print("Calling B's methodB")

		
>>> class C(A, B):
	def methodC(self):
		print("Calling C's methodC")
	def method(self):
		print("Calling C's overridden method")
		super().method()

		
>>> c = C()
>>> c.methodA()
Calling A's methodA
>>> c.methodB()
Calling B's methodB
>>> c.methodC()
Calling C's methodC
>>> c.method()
Calling C's overridden method
Calling A's method
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> class NasdaqStock:
	"""Class for NASDAQ stocks"""
	count = 0
	def __init__(self, symbol, price):
	    """Constructor for NasdaqStock"""
	    self.symbol = symbol
	    self.price = price
	    NasdaqStock.count += 1
	    print('Calling __init__({}, {:.2f}) > count: {}'.format\
		  (self.symbol, self.price, NasdaqStock.count))

	    
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> class NasdaqStock:
	"""Class for NASDAQ stocks"""
	count = 0
	def __init__(self, symbol, price):
	    """Constructor for NasdaqStock"""
	    self.symbol = symbol
	    self.price = price
	    NasdaqStock.count += 1
	    print('Calling __init__({}, {:.2f}) > count: {}'.format\
		  (self.symbol, self.price, NasdaqStock.count))

	def __del__(self):
		"""Destructor for NasdaqStock"""
		print('Calling __del__({})'.format(self))

		
>>> gg = NasdaqStock('GOOG', 1154.05)
Calling __init__(GOOG, 1154.05) > count: 1
>>> del(gg)
Calling __del__(<__main__.NasdaqStock object at 0x0000024ADB02DB20>)
>>> ms = NasdaqStock('MSFT', 102.44)
Calling __init__(MSFT, 102.44) > count: 2
>>> del(ms)
Calling __del__(<__main__.NasdaqStock object at 0x0000024ADB02DB20>)
>>> amz = NasdaqStock('AMZN', 1746.00)
Calling __init__(AMZN, 1746.00) > count: 3
>>> del(amz)
Calling __del__(<__main__.NasdaqStock object at 0x0000024ADB02DB20>)
>>> 