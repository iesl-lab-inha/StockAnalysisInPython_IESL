import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
 
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']}) # 새로운 데이터프레임 만들어줘서 크기를 맞춰줌 단 빈칸 존재
# 결측값 채우기 (ffill 앞에 있는 값으로 채우기, bfill 뒤에 있는 값으로 채우기) 결국 앞뒤 다 채워서 빈칸 없애기
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
# 점으로 산점도 확인
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
