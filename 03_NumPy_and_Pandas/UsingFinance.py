from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override() #Data를 다운 받는 함수

sec = pdr.get_data_yahoo('005930.KS', start='2022-06-01') #삼성전자의 22년 7월 1일부터의 주식 데이터(기존의 yfinance에서 변경된 부분이 있으므로 반드시 upgrade!!
msft = pdr.get_data_yahoo('MSFT', start='2022-06-01') #마이크로소프트의 22년 7월 1일 부터의 주식 데이터

print(sec.head(10)) #6월1일부터 삼성전자의 주가
print('\n')

tmp_msft = msft.drop(columns='Volume')#Volume 열을 제외
print(tmp_msft.tail()) #tail()함수는 제일 뒤 행을 보여줌
print(sec.index) #삼성전자의 index
print(sec.columns) #columns에 대한 정보
print('\n')

print(sec['Close'].shift(1)) #1행 뒤로 이동한 후의 결과, INDEX는 움직이지않고 Data만 움직임
print('\n')

sec_dpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100 #일간변동률 구하는 수식을 구현하였음.
#sec_dpc.iloc[0] = 0 #dpc의 첫번째 원소는 0
print(sec_dpc.head()) #앞부분 5개 출력
print(sec_dpc.describe())
#count는 전체 데이터 개수, std는 표준편차

sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100 #누적곱 계산. 계산해보니 최종적으로 -14.24%의 손실을 기록했음을 알 수 있음.
print(sec_dpc_cp)
print('\n')

msft_dpc = (msft['Close'] - msft['Close'].shift(1))/msft['Close'].shift(1) * 100 #마소의 일간 변동률
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100 #마소의 일간변동률의 누적곱
print(msft_dpc_cp)

import matplotlib.pyplot as plt
plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics') #삼성전자의 그래프 형태 코드
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft') #마소의 그래프 형태 코드
plt.legend(loc='best') #주석, 범주의 위치를 최선의 곳에 배치하라는 legened(loc='bset')
plt.show()

#2 히스토그램
plt.hist(sec_dpc, bins=18, label='Samsung daily percent change') #히스토그램 생성 함수
plt.grid(True) #그리드 생성
plt.legend(loc='best') #주석 가장 최선의 곳에 달기
plt.show()

#3 주식수익률 비교 그래프
plt.title("Samsung VS Microsoft (2022.06.01 ~ )") #제목
plt.plot(sec.index, sec_dpc_cp, 'b--', label="Samsung Electronics")#x축의 삼성전자의 index, y축은 일간수익률의 누적곱, 파란 점선, 그리고 선의 설명은 삼성전자.
plt.plot(msft.index, msft_dpc_cp, 'r--', label="Microsoft") #x축은 마소의 index, y축은 일간수익률의 누적곱, 빨간 점선, 그리고 선의 설명은 마소
plt.ylabel('Change %') #y축 설명은 변화율
plt.legend(loc='best') #가장 좋은 위치에 주석 달기
plt.grid(True) #격자 허용
plt.show()