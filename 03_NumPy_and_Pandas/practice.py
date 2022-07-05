# pip install numpy

import numpy as np
A = np.array([[1, 2],[3, 4]])
# 배열 차원
print(A.ndim)
# 배열 크기
print(A.shape)
# 원소 자료형
print(A.dtype)
# 접근 방식은 배열과 동일
# 1 보다 큰 index
print(A[A > 1])
# 전치
print(A.transpose())
# A.T()
# 평탄화 1차원  배열 형태로 Change
print(A.flatten())
B = np.array([10, 100])
# 배열 연산 같은 index끼리 + - * /
# 내적
print(A.dot(B))
'''
result
2
(2, 2)
int32
[2 3 4]
[[1 3]
 [2 4]]
[1 2 3 4]
[210 430]
'''

import pandas as pd

#pandas series 생성
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
# append 뒤에 추가
s = s.append(ser)
print(s)

# index 값(-1은 제일 마지막값)
print(s.index[-1])
# index에 데이터
print(s.values[-1])
# 인덱서 해당하는 데이터를 표시
print(s.loc[8.0])
# 위를 index로
print(s.iloc[-1])
# : 복수개 출력
print(s.values[:])
# index 삭제
s.drop(8.0)
print(s)
print(s.describe())

# 표시
import matplotlib.pyplot as plt

plt.title("test")
plt.plot(s, "bs--")
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()

'''
result
0    0.0
1    3.6
2    2.0
3    5.8
4    4.2
5    8.0
dtype: float64
0.0    0.0
1.0    3.6
2.0    2.0
3.0    5.8
4.0    4.2
5.0    8.0
6.8    6.7
8.0    4.2
dtype: float64
8.0
4.2
4.2
4.2
[0.  3.6 2.  5.8 4.2 8.  6.7 4.2]
0.0    0.0
1.0    3.6
2.0    2.0
3.0    5.8
4.0    4.2
5.0    8.0
6.8    6.7
8.0    4.2
dtype: float64
count    8.000000
mean     4.312500
std      2.563166
min      0.000000
25%      3.200000
50%      4.200000
75%      6.025000
max      8.000000
dtype: float64

그래프 on
'''

import pandas as pd

df = pd.DataFrame({'KOSPI' : [1915, 1961, 2026, 2467, 2041], 'KOSDAQ' : [542, 682, 631, 798, 675]})
print(df)
print(df.describe())
print(df.info())

#각 시리즈를 이용해 dataframe 생성 가능
rows = []
columns = ['name1', 'name2']
index = []
df = pd.DataFrame(rows, columns=columns, index=index)

# 데이터 for문 출력
for i in df.index:
    print(i, df['name1'][i], df['name2'][i])

for row in df.itertuples(name='KRX'):
    print(row)

for row in df.itertuples():
    print(row[0], row[1], row[2])

for idx, row in df.iterrows():
    print(idx, row[0], row[1])





# .head()  .tail
# plot.(x, y, 마커형태[, label='label'])
# plt.legend(loc='best') -> 그래프가 표시되지않는 부분을 찾아서 적절환 위체에 범례를 표시