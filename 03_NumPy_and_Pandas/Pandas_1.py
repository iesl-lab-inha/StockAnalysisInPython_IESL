import pandas as pd
s = pd.Series([0.0, 1.2, 2.4, 3.6, 5.4, 8.1]) #List로 나타낸 Series
print(s) #인덱싱 설정 해주지 않아서 0~5로 인덱싱 되었음
print('\n')

s.index = pd.Index([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) #Index 새롭게 설정
s.index.name = 'NEW_INDEX' #Index 이름
s.name = 'NEW_SERIES' #Series 이름
s[3.4]=3.4 #Add Index, Numbering과 상관없음 뒤에 그냥 붙음
s[7.0]=9.0
print(s)
print('\n')

a = pd.Series([12.2, 13.4], index=[6.8, 10.2]) #New Series
s = s.append(a) #append A series to s series
s.index.name = 'a+s index' # naming new index
s.name = 's+a series' #naming new series
print(s)
print('\n')

print(s.index[-1]) #10.2
print(s.values[-1]) #13.4 , 위 두 line 지정해준 new index가 아닌 기존 index 방식
print(s.loc[6.0]) #8.1
print(s.iloc[-1]) #8.1

print('\n')
print(s.values[:]) #Vector로 반환
print(s.iloc[:]) #Series로 반환

print('\n')
print(s.describe()) #Data 출력

print('\n')
import matplotlib.pyplot as plt
plt.title("Series_To_Graph") #Graph 이름
plt.plot(s,'gs--') #구성, s Series를 Blue, 점선으로 (rs로 하면 빨간색,gs는 초록선, - 로 하면 실선)
plt.xticks(s.index) #x축
plt.yticks(s.values) #y축
plt.grid(True) #격자를 어떻게 할것인지
plt.show() #출력