import pandas as pd
import requests
from bs4 import BeautifulSoup
import mplfinance as mpf

#맨 뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1' #셀트리온 일별 시세 첫 페이지
html = requests.get(url, headers = {'User-agent': 'Mozilla/5.0'}).text #웹 스크레이핑을 위해, request 라이브러리를 이용하여 웹페이지 요청
bs = BeautifulSoup(html, 'lxml') #뷰티풀수프 생성자의 첫번째 인수로 HTML/XML페이지를 넘기고 두번째 인수로 페이지 파싱 방식
pgrr = bs.find('td', class_='pgRR') #find함수로 class 속성이 'pgRR'인 td 태그를 찾음
s = str(pgrr.a['href']).split('=') #<a>태그의 href 속성값(문자열 링크)을 얻어 문자열 구분
last_page = s[-1] #맨 뒤 페이지 숫자(전체 페이지 수)

#전체 페이지 읽어오기
df = pd.DataFrame() #데이터프레임형 df변수
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=068270' #시세확인 url
for page in range(1, int(last_page)+1): #1부터 last_page 까지 반복
    url = '{}&page={}'.format(sise_url, page) #page로 요청할 URL 페이지수 변경(format이용)
    html = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}).text #웹페이지 요청
    df = df.append(pd.read_html(html, header=0)[0]) #한 페이지 분량의 데이터프레임을 df객체에 추가

#차트 출력을 위해 데이터 프레임 가공하기
df = df.dropna() #NaN행 제거
df = df.iloc[0:30] #최근 데이터 30행 사용
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'}) #한글 칼럼명을 영문 칼럼명으로 변경
df = df.sort_values(by='Date') #날짜 순 오름차순 정렬
df.index = pd.to_datetime(df.Date) #Date칼럼을 DatetimeIndex형으로 변경한 후 인덱스로 설정
df = df[['Open', 'High', 'Low', 'Close', 'Volume']] #데이터프레임 구조 변경

#엠피엘파이낸스로 캔들차트 그리기
mpf.plot(df, title='Celltrion candle chart', type='candle') #캔들 차트 출력

mpf.plot(df, title='Celltrion ohlc chart', type='ohlc') #OHLC 차트 출력

kwargs = dict(title='Celltrion customized chart', type='candle',
              mav=(2,4,6), volume=True, ylabel='ohlc candles') #mpf.plot()함수를 호출할 떄 쓰이는 여러 인수를 담은 딕셔너리 생성
mc = mpf.make_marketcolors(up='r', down='b', inherit=True) #마켓 색상 지정
s = mpf.make_mpf_style(marketcolors=mc) #스타일 객체 생성
mpf.plot(df, **kwargs, style=s) #차트 출력
