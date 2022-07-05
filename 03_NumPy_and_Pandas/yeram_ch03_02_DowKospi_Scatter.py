import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') #2000년 이후 다우존스 지수 데이터 다운로드
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') #2000년 이후 KOSPI 지수 데이터 다운로드

df = pd.DataFrame({'DOW':dow['Close'], 'KOSPI':kospi['Close']}) #데이터 프레임 생성(데이터 사이즈 맞추기)
df = df.fillna(method='bfill') #NaN 없애기(bfill방식)
df = df.fillna(method='ffill') #마지막행의 NaN까지 없애기(ffill방식))

import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.') #산점도 그리기
plt.xlabel=('Dow Jones Industrial Average')
plt.ylabel=('KOSPI')
plt.show()
