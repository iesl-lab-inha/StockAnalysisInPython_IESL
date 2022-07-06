Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import timeit
>>> iteration_test = """
for i in itr :
    pass
    """
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
0.18440029999999297
>>> timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000)
0.09723350000000153
>>> timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000)
0.17384430000001316
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> import timeit
>>> iteration_test = """
for i in itr :
    pass
"""
>>> timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000)
0.21408740000000037
>>> timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000)
0.19103640000000155
>>> timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000)
0.1276818999999989
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> import timeit
>>> search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr :
   pass
   """
>>> timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000)
0.002852600000011307
>>> timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000)
0.14549729999998817
>>> timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000)
0.08817129999999906
>>> 