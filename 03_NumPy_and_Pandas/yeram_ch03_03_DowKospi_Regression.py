import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats
import matplotlib.pylab as plt

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') #다우존스 지수 다운로드  
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') #KOSPI지수 다운로드

df = pd.DataFrame({'X':dow['Close'], 'Y':kospi['Close']}) #다우존스 지수를 X, KOSPI지수를 Y탈럼으로 갖는 데이터 프레임 생성
df = df.fillna(method='bfill') #NaN 제거
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y) #선형회귀 모델 객체 생성
regr_line = f'Y = {regr.slope:2f}  X + {regr.intercept:2f}' #범례에 회귀식 표시

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')  #산점도를 작은 원으로 나타냄
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r') #회귀선을 붉은 색으로 그림
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
