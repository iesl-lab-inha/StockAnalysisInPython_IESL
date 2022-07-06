import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from scipy import stats
import matplotlib.pylab as plt
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04') #다우존스 데이터 추출
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') #코스피 데이터 추출

df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']}) #dow와 kospi 종가로 데이터프레임 만들기
df = df.fillna(method='ffill') #NaN제거
df = df.fillna(method='bfill')
print(df.corr()) #상관계수 구하기 , 상관계수 = 0.824918
print('\n')

print(df['X'].corr(df['Y'])) #상관계수 구하는 2번째 방법, Using Series

r_value=df['X'].corr(df['Y'])**2 #결정계수 : 상관계수의 제곱
print(r_value)

#다우존스 지수와 KOSPI 의 회귀분석
model = stats.linregress(df.X, df.Y) #선형회귀모델 객체 생성
model_line = f'Y = {model.slope:.2f}*X + {model.intercept:.2f}' #선형회귀를 통해 구한 Y기대치, model_line으로 선언 기울기와 y절편 소수 2번재까지 노출
plt.figure(figsize=(7,7)) #그래프 크기
plt.plot(df.X, df.Y, '.') #x축 dow, y축 kospi를 점으로 표현
plt.plot(df.X, model.slope*df.X + model.intercept, 'r') #x축 dow, Y의기대치를 빨간선으로 표현
plt.legend(['DOW X KOSPI', model_line]) #주석을 Dow x KOSPI, Y의 기대치로 작성
plt.title(f'DOW X KOSPI (R={model.rvalue:.2f})') #제목 작성 이때 상관계수도 명시해줌. 소수2번재 자리까지 노출
plt.xlabel('Dow Jones Industrial Average') #x축 설명
plt.ylabel('KOSPI') #y축 설명
plt.show()

#임의의 X: Dow Jones 값을 통해 Y: Kospi의 값을 예측할 수 있다.