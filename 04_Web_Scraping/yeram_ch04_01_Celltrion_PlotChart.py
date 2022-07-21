import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

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
df = df.sort_values(by='날짜') #날짜 순 오름차순 정렬

#닐짜, 종가, 칼럼으로 차트 그리기
plt.title('Celltrion (close)') #차트 제목
plt.xticks(rotation=45) #x축 레이블 45도 회전
plt.plot(df['날짜'], df['종가'], 'co-') #x축은 날짜데이터, y축은 종가데이터, 청록색 원(co), 실선(-)
plt.grid(color='gray', linestyle='--') #회색 점선 격자
plt.show() #차트 출력
