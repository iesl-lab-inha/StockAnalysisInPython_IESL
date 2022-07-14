import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = 'https://finance.naver.com/item/sise_day.naver?code=035720&page=1'
html = requests.get(url, headers={'User-agent':'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=035720'
for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = df.append(pd.read_html(html, header=0)[0])

df = df.dropna() #NaN 제거
df = df.iloc[0:30] # 30개의 종가 데이터 사용 , 슬라이싱
df = df.sort_values(by='날짜') #날짜순으로 배열, 오름차순

plt.title('KAKAO(Close)')
plt.xticks(rotation=45) #겹치는 경우가 있으므로 x축의 텍스트 방향을 45도로 기울여 사용
plt.plot(df['날짜'], df['종가'], 'co-') #x축은 날짜, y축은 종가로 하여 그래프 생성, 'co-' 는 좌표를 초록점으로, 점끼리 잇는 선을 실선으로
plt.grid(color='gray', linestyle='--') # 그리드는 회색 점선으로 표현
plt.show()