import pandas as pd
import requests
from bs4 import BeautifulSoup
import mplfinance as mpf

url = 'https://finance.naver.com/item/sise_day.naver?code=035420&page=1'
html = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=035420'

for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = df.append(pd.read_html(html, header=0)[0])

df = df.dropna() #NaN제거
df = df.iloc[0:30] #0부터30번째 까지 슬라이싱
df = df.rename(columns={'날짜': 'Date', '시가' : 'Open', '고가' : 'High' , '저가' : 'Low' , '종가' : 'Close' , '거래량' : 'Volume'}) #이름을 재정의하기, 한글칼럼명을 영문칼럼명으로 변경
df = df.sort_values(by='Date') #날짜별로 오름차순으로 정렬
df.index = pd.to_datetime(df.Date) #인덱스를 Date칼럼으로 변경
df = df[['Open', 'High', 'Low', 'Close', 'Volume']] #해당 열만 갖도록 데이터프레임 구조 수정

mpf.plot(df, title='Naver Candle chart') #캔들차트 출력
#mpf.plot(df, title='Naver ohlc chart', type='ohlc') : ohlc차트로 출력

#이동 평균선 삽입
kwargs = dict(title='Naver customized chart', type = 'candle', mav=(2, 4, 6), volume=True, ylabel='ohlc candles') #kwargs는 keyword arguments의 약자, 여러 인수를 담는 딕셔너리
mc = mpf.make_marketcolors(up='r', down='b', inherit=True) #마켓 색상은 스타일을 지정하는 필수 객체 , 상승 : 빨강, 하강: 파랑
s = mpf.make_mpf_style(marketcolors=mc) #마켓색상을 인수로 갖는 스타일 객체 완성
mpf.plot(df, **kwargs, style=s) #df을 x축으로 갖고, 여러인수를 y축으로 가지며 style이 s인 그래프 완성