Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requests
>>> url = 'https://finance.naver.com/item/sise_day.naver?code=068270&page=1'
>>> html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
>>> bs = BeautifulSoup(html, 'lxml')
>>> pgrr = bs.find('td', class_='pgRR')
>>>  print(pgrr.a['href'])
 
SyntaxError: unexpected indent
>>> print(pgrr.a['href'])
/item/sise_day.naver?code=068270&page=421
>>> print(pgrr.prettify())
<td class="pgRR">
 <a href="/item/sise_day.naver?code=068270&amp;page=421">
  맨뒤
  <img alt="" border="0" height="5" src="https://ssl.pstatic.net/static/n/cmn/bu_pgarRR.gif" width="8"/>
 </a>
</td>

>>> print(pgrr.text)

맨뒤
				


>>> s = str(pgrr.a['href']).split('=')
>>> last_page = s[-1]
>>> last_page
'421'
>>> df = pd.DataFrame()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df = pd.DataFrame()
NameError: name 'pd' is not defined
>>> import warnings
>>> warnings.simplefilter(action='ignore', category=FutureWarning)
>>> import pandas as pd
>>> df = pd.DataFrame()
>>> sise_url = 'https://finance.naver.com/item/sise.naver?code=068270'
>>> for page in range(1, int(last_page)+1):
	url = '{}&page={}'.format(sise_url, page)
	html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
	df = df.append(pd.read_html(html, header=0)[0])
	df = df.dropna()

	
>>> print(df)
   전일  190,000  190,000  ...     거래량  418,170  418,170
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
..                  ...  ...                       ...
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만
0    시가  190,000190,000  ...  거래대금  78,700  78,700  백만

[421 rows x 3 columns]
>>> import warnings
>>> warnings.simplefilter(action='ignore', category=FutureWarning)
>>> import pandas as pd
>>> df = pd.DataFrame()
>>> sise_url = 'https://finance.naver.com/item/sise.day.nhn?code=068270'
>>> for page in range(1, int(last_page)+1):
	url = '{}&page={}'.format(sise_url, page)
	html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
	df = df.append(pd.read_html(html, header=0)[0])
	df = df.dropna()

	
Traceback (most recent call last):
  File "<pyshell#36>", line 4, in <module>
    df = df.append(pd.read_html(html, header=0)[0])
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\io\html.py", line 1113, in read_html
    return _parse(
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\io\html.py", line 939, in _parse
    raise retained
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\io\html.py", line 919, in _parse
    tables = p.parse_tables()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\io\html.py", line 239, in parse_tables
    tables = self._parse_tables(self._build_doc(), self.match, self.attrs)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\io\html.py", line 569, in _parse_tables
    raise ValueError("No tables found")
ValueError: No tables found
>>> import warnings
>>> warnings.simplefilter(action='ignore', category=FutureWarning)
>>> import pandas as pd
>>> df = pd.DataFrame()
>>> sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
>>> for page in range(1, int(last_page)+1):
	url = '{}&page={}'.format(sise_url, page)
	html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
	df = df.append(pd.read_html(html, header=0)[0])
	df = df.dropna()

	
>>> print(df)
            날짜        종가     전일비        시가        고가        저가       거래량
1   2022.07.14  189000.0  1000.0  190000.0  190500.0  186500.0  418170.0
2   2022.07.13  190000.0  2500.0  188500.0  193000.0  187500.0  513629.0
3   2022.07.12  187500.0  1500.0  187500.0  191500.0  185000.0  423296.0
4   2022.07.11  186000.0  3500.0  181500.0  187500.0  181500.0  344098.0
5   2022.07.08  182500.0  5000.0  187000.0  187000.0  178500.0  755595.0
..         ...       ...     ...       ...       ...       ...       ...
11  2005.07.25    5650.0    70.0    5500.0    5950.0    5500.0   61036.0
12  2005.07.22    5580.0   160.0    5850.0    5850.0    5530.0   69921.0
13  2005.07.21    5740.0   810.0    6450.0    6580.0    5730.0  182685.0
1   2005.07.20    6550.0  1150.0    7690.0    7690.0    6550.0  422688.0
2   2005.07.19    7700.0  2500.0    6700.0    7700.0    6510.0  499088.0

[4202 rows x 7 columns]
>>> 