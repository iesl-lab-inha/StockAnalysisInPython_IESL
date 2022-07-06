import pandas as pd
import yfinance as yf
from scipy import stats
import matplotlib.pylab as plt
from pandas_datareader import data as pdr
yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') #코스피 지수 추출
tlt = pdr.get_data_yahoo('TLT', '2002-07-30') #미국국채 데이터 추출

df = pd.DataFrame({'X': tlt['Close'], 'Y': kospi['Close']}) #각 종목의 종가를 DataFrame으로 형성
df = df.fillna(method='ffill') #NaN의 값을 ffill 과 bfill값으로 대체
df = df.fillna(method='bfill')

model = stats.linregress(df.X, df.Y) #선형회귀모델 객체 생성
model_line = f'Y={model.slope:.2f}*X + {model.intercept:.2f}' #fstring 사용해서 중괄호안에 수식 대입하기. Y 기대치 수식

plt.figure(figsize=(7,7)) #그래프 크기 지정
plt.plot(df.X, df.Y, 'x') #메인 그래프 설정 x축은 tlt, y축은 코스피, 점대신 x자 모양으로 나타내기
plt.plot(df.X, model.slope*df.X+model.intercept, 'r') #x축은 tlt, 빨간색 선으로 기대치 수식 그래프화
plt.legend(['TLT X KOSPI', model_line]) #범례를 다음과 같이 설정
plt.title(f'TLT X KOSPI (R={model.rvalue:.2f})') #f string 사용해서 중괄호안에 수식 대입하기. 그래프의 타이틀
plt.xlabel('iShares Barclays 20+ YrTreas.Bond(TLT)') #그래프의 x축 설명
plt.ylabel('KOSPI') #그래프의 y축 설명
plt.show()