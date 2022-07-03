import numpy as np
A = np.array([[1, 2], [3, 4]]) #행렬 A
print(A)
B= np.array([[1, 2, 3], [4, 5, 6]]) #행렬 B
print(B)

print('\n')
print(type(A)); print(type(B)) #타입 확인
print('\n')
print(A.ndim); print(B.ndim) #차원 확인
print('\n')
print(A.shape); print(B.shape) #행, 열 확인
print('\n')
print(A[0]); print(B[1]) #인덱싱
print('\n')
print(A[0,1]); print(B[1,2]) #다차원 인덱싱
print('\n')
print(A.T); print(B.T) #전치행렬
print('\n')
print(A+A); print(np.add(A,A)) #행렬의 덧셈
#print(A+B) makes error.
print('\n')
C = np.array([10, 100])#broadcast
print(A*C)
print('\n')
D = np.array([1, 2, 3])
#print(A*D) = error
print('\n')
print(A.dot(B)) #내적
print('\n')
print(A.dot(C)) #내적, 행벡터를 열벡터로 가정하였음.