from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04') #코스피(^KS11)데이터 다운로드

window = 252 # 산정 기간
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() #KOSPI 종가 칼럼에서 1년 기간 단위로 최고치 구하기
drawdown = kospi['Adj Close']/peak - 1.0 # 최고치 대비 현재 KOSPI종가가 얼마나 하락했는지 구함
max_dd = drawdown.rolling(window, min_periods=1).min()# drawdownd에서 1년 기간동안 최저치를 구함 = 최저 손실 낙폭

plt.figure(figsize=(9,7)) #창 사이즈
plt.subplot(211) #2행 1열 중 1행
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) #2행 1열 중 2행
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()
