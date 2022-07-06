from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04') #코스피지수 데이터 다운로드

window = 252 #윈도우 크기 : 1년동안의 개장일을 252일로 어림
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() #종가칼럼에서 1년 기간단위로 최고치 peak구함
drawdown = kospi['Adj Close']/peak - 1.0 #peak대비 코스피종가가 얼마나 하락했는지 구함
max_dd = drawdown.rolling(window, min_periods=1).min() #1년단위로 최저치를구하며, 마이너스이므로 최저치가 최대손실낙폭

plt.figure(figsize=(9, 7)) #그래프의 크기를 정하는 함수
plt.subplot(211) #하나의 이미지 파일에 2행 1열의 첫번째 그래프를 작성
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True) #코스피의 종가를 나타내는 그래프
plt.subplot(212) #2행 1열의 두번째 그래프를 작성
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True) #drawdown 그래프 작성
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True) #max_dd그래프 작성
plt.show()

print(max_dd.min()) #최소 MDD
print(max_dd[max_dd==max_dd.min()]) #최소 MDD의 날짜