Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import requests
>>> from bs4 import BeautifulSoup
>>> from matplotlib import pyplot as plt
>>> url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
>>> html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
>>> bs = BeautifulSoup(html, 'lxml')
>>> pgrr = bs.find('td', class_='pgRR')
>>> s = str(pgrr.a['href']).split('=')
>>> last_page = s[-1]
>>> df = pd.DataFrame()
>>> sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
>>> import warnings
>>> warnings.simplefilter(action='ignore', category=FutureWarning)
>>> for page in range(1, int(last_page)+1):
	url = '{}&page={}'.format(sise_url, page)
	html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
	df = df.append(pd.read_html(html, header=0)[0])

	
>>> df = df.dropna()
>>> df = df.iloc[0:30]
>>> df = df.sort_values(by='날짜')
>>> plt.title('Celltrion (close)')
Text(0.5, 1.0, 'Celltrion (close)')
>>> plt.xticks(rotation=45)
(array([0. , 0.2, 0.4, 0.6, 0.8, 1. ]), <a list of 6 Text xticklabel objects>)
>>> plt.plot(df['날짜'], df['종가'], 'co-')
[<matplotlib.lines.Line2D object at 0x0000026C1C815820>]
>>> plt.grid(color='gray', linestyle='--')
>>> plt.show()
>>> 