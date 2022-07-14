Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> A = np.array([[1, 2], [3, 4]])
>>> A
array([[1, 2],
       [3, 4]])
>>> A.T
array([[1, 3],
       [2, 4]])
>>> A
array([[1, 2],
       [3, 4]])
>>> A.flatten()
array([1, 2, 3, 4])
>>> A
array([[1, 2],
       [3, 4]])
>>> A + A
array([[2, 4],
       [6, 8]])
>>> A - A
array([[0, 0],
       [0, 0]])
>>> A * A
array([[ 1,  4],
       [ 9, 16]])
>>> A / A
array([[1., 1.],
       [1., 1.]])
>>> A
array([[1, 2],
       [3, 4]])
>>> B = np.array([10, 100])
>>> 
>>> A * B
array([[ 10, 200],
       [ 30, 400]])
>>> B.dot(B)
10100
>>> A.dot(B)
array([210, 430])
>>> 