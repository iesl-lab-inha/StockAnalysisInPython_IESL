import pandas as pd
df = pd.DataFrame({'Haewon': [160, 165, 170, 175, 179], 'Hyesoo': [150, 151, 153, 156, 159]},
                  index = [2016, 2017, 2018, 2019, 2020]) #딕셔너리 사용한 데이터프레임
print(df)
print(df.describe())
print(df.info())
print('\n')

haewon = pd.Series([160, 165, 170, 175, 179], index = [2016, 2017, 2018, 2019, 2020], name = 'Haewon') #Series로 데이터프레임 만들기
hyesoo = pd.Series([150, 151, 153, 156, 159], index = [2016, 2017, 2018, 2019, 2020], name = 'Hyesoo')
ndf = pd.DataFrame({haewon.name : haewon, hyesoo.name : hyesoo}) #Series Dictionary화
print(ndf)
print('\n')

columns = ['Haewon', 'Hyesoo'] #List 사용해서 데이터프레임만들기
index = [2016, 2017, 2018, 2019, 2020] #index List
rows = [] #행 List
rows.append([160, 150]) #행 추가
rows.append([165, 151])
rows.append([170,153])
rows.append([175, 156])
rows.append([179, 159])
ldf = pd.DataFrame(rows, columns=columns, index=index) #데이터 프레임만들기, 데이터=행, 열=열, 인덱스=인덱스
print(ldf)
print('\n')

for i in df.index : #일반적인 순회방법. 데이터프레임의 index를 반복하여 나타냄
    print(i, df['Haewon'][i], df['Hyesoo'][i])
print('\n')

for row in df.itertuples(name='Height'): #itertuples를 사용해 튜플형태로 순회
    print(row)

print('\n')
for row in df.itertuples(): #itertuple의 보통 사용법. 첫번째 row 부터 마지막 row까지 반복
    print(row[0], row[1], row[2])

print('\n')
for idx, row in df.iterrows(): #iterrows의 사용법, 첫번째 idx, row부터 마지막까지 반복
    print(idx, row[0], row[1])

import matplotlib.pyplot as plt #3.2 복습
plt.title("Height_HW_HS")
plt.plot(haewon,'rs--', hyesoo , 'bs--')
plt.xticks(haewon.index)
plt.yticks(haewon.values)
plt.grid(True)
plt.show()