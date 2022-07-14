from bs4 import BeautifulSoup
import pandas as pd
import requests
url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
html = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml') #첫번째 인수로 html/xml 페이지 넘겨주고, 두번째 인수로 파싱할 방법 : lxml (속도가 매우 빠르고 유연한 파싱) 선택
pgrr = bs.find('td', class_='pgRR') #find함수를 통해 마지막 페이지를 탐색
print(pgrr.a['href']) #html 속성을 사용해 맨뒤 페이지 획득
print(pgrr.prettify()) #pgRR의 전체 텍스트 확인
print(pgrr.text) #태그를 제외한 text부분
s = str(pgrr.a['href']).split('=') #split함수를 사용해 리스트로 나타내기
print(s)
last_page = s[-1] #해당 리스트에서 마지막 인덱스 호출 = 마지막 페이지
print(last_page); print('\n')

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=005930' #시세확인 url

for page in range(1, int(last_page)+1): #1부터 마지막페이지+1 까지 반복
    url = '{}&page={}'.format(sise_url, page) #url은 format함수를 사용함
    html = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}).text #request 라이브러리 사용, 웹페이지 요청
    df = df.append(pd.read_html(html, header=0)[0]) #요청한 웹페이지 분량의 데이터프레임을 추가

df = df.dropna() #NaN행 제거
print(df)