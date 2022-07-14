Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> A = np.array([[1, 2], [3, 4]])
>>> A
array([[1, 2],
       [3, 4]])
>>> 
>>> type(A)
<class 'numpy.ndarray'>
>>> 
>>> A.ndim
2
>>> A.shape
(2, 2)
>>> 
>>> A.dtype
dtype('int32')
>>> 
>>> print(A.max(), A.mean(), A.min(), A.sum())
4 2.5 1 10
>>> 
>>> A[0]; A[1]
array([1, 2])
array([3, 4])
>>> print(A[0][0], A[0][1]); print(A[1][0], A[1][1])
1 2
3 4
>>> print(A[0, 0], A[0, 1]); print(A[1, 0], A[1, 1])
1 2
3 4
>>> A[A>1]
array([2, 3, 4])
>>> 