from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
 
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04') #삼성전자 주식 데이터 가져오기(2018-05-04~2022-07-05)
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100 #삼성전자 일간 변동률 구하기
sec_dpc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100 # 일간 변동률 누적곱 계산

msft = pdr.get_data_yahoo('MSFT', start='2018-05-04') #마이크로소프트 주식 데이터 가져오기(2018-05-04~2022-07-05)
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100 #마이크로 소프트 일간 변동률 구하기
msft_dpc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100 # 일간 변동률 누적곱 계산
 
import matplotlib.pyplot as plt
plt.plot(sec.index, sec_dpc_cp, 'b', label='Samsung Electronics') #x좌표: 삼성전자 데이터프레임의 날짜 인덱스, y좌표: 삼성전자 데이터프레임의 종가 데이터, 푸른 색 실선
plt.plot(msft.index, msft_dpc_cp, 'r--', label='Microsoft') #x좌표: msft 데이터프레임의 날짜 인덱스, y좌표: msft 데이터프레임의 종가 데이터, 붉은 색 점선
plt.ylabel('Change %') #y축 label
plt.grid(True) #눈금 표시
plt.legend(loc='best') #범례의 위치, 적절한 위치에 범례 표시
plt.show() 
