from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100 # 일간 변동률 누적곱 계산
print(sec_dpc_cp)


msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100

'''
새로운 방법으로 data 추출
'''

import matplotlib.pyplot as plt
plt.plot(sec.index, sec_dpc_cp, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cp, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()

'''
plt 조작하는 함수, 요소들 check
'''

# 증권사에서 직접 정보를 가져오기 위해서는 32bit 필요
# 네이버 크롤링
import requests
from bs4 import BeautifulSoup
import pandas as pd

def naver_data(

):
    url ="https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    # 저 주소에 html 모두 프린트
    # print(soup)

    #봉데이터만 추출출

    code = '005930'  # 삼성전자 종목코드
    url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
    headers = {'User-agent': 'Mozilla/5.0'}  # 웹브라우저 접속처럼 인식시키기 위해 정보 추가
    req = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(req.text, 'html.parser')
    pgrr = bs.find('td', class_='pgRR')

    page_no = 10
    last_page = int(pgrr.a["href"].split('=')[-1])
    print(last_page)
    pages = min(last_page, page_no)  # 마지막 페이지와 가져올 페이지 수 중에 작은 값 선택
    df = pd.DataFrame()

    for page in range(1, pages + 1):
        page_url = '{}&page={}'.format(url, page)
        df = df.append(pd.read_html(requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])
    df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff'
        , '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})  # 영문으로 컬럼명 변경
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()  # 결측치 제거
    df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[
        ['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)  # BIGINT형으로 지정한 컬럼을 int형으로 변경
    df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
    df = df.sort_values(by='date')  # 날짜순으로 정렬

    print(df)

    # https://scribblinganything.tistory.com/383




naver_data()