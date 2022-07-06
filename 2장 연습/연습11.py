Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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

		
>>> help(NasdaqStock)
Help on class NasdaqStock in module __main__:

class NasdaqStock(builtins.object)
 |  NasdaqStock(symbol, price)
 |  
 |  Class for NASDAQ stocks
 |  
 |  Methods defined here:
 |  
 |  __del__(self)
 |      Destructor for NasdaqStock
 |  
 |  __init__(self, symbol, price)
 |      Constructor for NasdaqStock
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  count = 0

>>> 