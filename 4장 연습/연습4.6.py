Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import requests
>>> from bs4 import BeautifulSoup
>>> from matplotlib import pyplot as plt
>>> from matplotlib import dates as mdates
>>> from mplfinance.original_flavor import candlestick_ohlc
>>> from datetime import datetime
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
>>> for idx in range(0, len(df)):
	dt = datetime.strptime(df['날짜'].values[idx], '%Y.%m.%d').date()
	df['날짜'].values[idx] = mdates.date2num(dt)

	
>>> ohlc = df[['날짜','시가','고가','저가','종가']]
>>> plt.figure(figsize=(9, 6))
<Figure size 900x600 with 0 Axes>
>>> ax = plt.subplot(1, 1, 1)
>>> plt.title('Celltrion (mpl_finance candle stick)')
Text(0.5, 1.0, 'Celltrion (mpl_finance candle stick)')
>>> candlestick_ohlc(ax, ohlc.values, width=0.7, colorup='red',
		 colordown='blue')
([<matplotlib.lines.Line2D object at 0x00000200290C8910>, <matplotlib.lines.Line2D object at 0x00000200290C8FD0>, <matplotlib.lines.Line2D object at 0x00000200290DB610>, <matplotlib.lines.Line2D object at 0x00000200290DBBE0>, <matplotlib.lines.Line2D object at 0x00000200290E71F0>, <matplotlib.lines.Line2D object at 0x00000200290E77C0>, <matplotlib.lines.Line2D object at 0x00000200290E7D90>, <matplotlib.lines.Line2D object at 0x00000200290F23A0>, <matplotlib.lines.Line2D object at 0x00000200290F2970>, <matplotlib.lines.Line2D object at 0x00000200290F2F40>, <matplotlib.lines.Line2D object at 0x00000200290FB580>, <matplotlib.lines.Line2D object at 0x00000200290FBB50>, <matplotlib.lines.Line2D object at 0x0000020029103160>, <matplotlib.lines.Line2D object at 0x0000020029103730>, <matplotlib.lines.Line2D object at 0x0000020029103D00>, <matplotlib.lines.Line2D object at 0x000002002910C310>, <matplotlib.lines.Line2D object at 0x000002002910C8E0>, <matplotlib.lines.Line2D object at 0x000002002910CEB0>, <matplotlib.lines.Line2D object at 0x00000200291184C0>, <matplotlib.lines.Line2D object at 0x0000020026222B80>, <matplotlib.lines.Line2D object at 0x0000020029118A60>, <matplotlib.lines.Line2D object at 0x00000200291221F0>, <matplotlib.lines.Line2D object at 0x00000200291227C0>, <matplotlib.lines.Line2D object at 0x0000020029122D90>, <matplotlib.lines.Line2D object at 0x000002002912B3A0>, <matplotlib.lines.Line2D object at 0x000002002912B970>, <matplotlib.lines.Line2D object at 0x000002002912BF40>, <matplotlib.lines.Line2D object at 0x0000020029135550>, <matplotlib.lines.Line2D object at 0x0000020029135B20>, <matplotlib.lines.Line2D object at 0x000002002913E130>], [<matplotlib.patches.Rectangle object at 0x00000200290C8AF0>, <matplotlib.patches.Rectangle object at 0x00000200290C8FA0>, <matplotlib.patches.Rectangle object at 0x00000200290DB730>, <matplotlib.patches.Rectangle object at 0x00000200290DBD00>, <matplotlib.patches.Rectangle object at 0x00000200290E7310>, <matplotlib.patches.Rectangle object at 0x00000200290E78E0>, <matplotlib.patches.Rectangle object at 0x00000200290E7EB0>, <matplotlib.patches.Rectangle object at 0x00000200290F24C0>, <matplotlib.patches.Rectangle object at 0x00000200290F2A90>, <matplotlib.patches.Rectangle object at 0x00000200290F2FA0>, <matplotlib.patches.Rectangle object at 0x00000200290FB6A0>, <matplotlib.patches.Rectangle object at 0x00000200290FBC70>, <matplotlib.patches.Rectangle object at 0x0000020029103280>, <matplotlib.patches.Rectangle object at 0x0000020029103850>, <matplotlib.patches.Rectangle object at 0x0000020029103E20>, <matplotlib.patches.Rectangle object at 0x000002002910C430>, <matplotlib.patches.Rectangle object at 0x000002002910CA00>, <matplotlib.patches.Rectangle object at 0x000002002910CEE0>, <matplotlib.patches.Rectangle object at 0x00000200291185E0>, <matplotlib.patches.Rectangle object at 0x0000020026222640>, <matplotlib.patches.Rectangle object at 0x0000020029118D00>, <matplotlib.patches.Rectangle object at 0x0000020029122310>, <matplotlib.patches.Rectangle object at 0x00000200291228E0>, <matplotlib.patches.Rectangle object at 0x0000020029122EB0>, <matplotlib.patches.Rectangle object at 0x000002002912B4C0>, <matplotlib.patches.Rectangle object at 0x000002002912BA90>, <matplotlib.patches.Rectangle object at 0x000002002912BFA0>, <matplotlib.patches.Rectangle object at 0x0000020029135670>, <matplotlib.patches.Rectangle object at 0x0000020029135C40>, <matplotlib.patches.Rectangle object at 0x000002002913E250>])
>>> ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
>>> plt.xticks(rotation=45)
(array([738300., 738310., 738320., 738330., 738340., 738350., 738360.]), <a list of 7 Text xticklabel objects>)
>>> plt.grid(color='gray', linestyle='--')
>>> plt.show()
>>> 