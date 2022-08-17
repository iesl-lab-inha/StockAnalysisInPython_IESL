import pandas as pd
#from bs4 import BeautifulSoup
#import urllib
#from urllib.request import urlopen
import pymysql
#import pandas.io.sql as sql
from datetime import datetime
from datetime import timedelta
#from threading import Timer
#import matplotlib.pyplot as plt

class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', password='abc12345', db='INVESTAR', charset='utf8')
        self.codes = dict()
        self.getCompanyInfo()
        
    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def getCompanyInfo(self):
        """company_info 테이블에서 읽어와서 companyData와 codes에 저장"""
        sql = "SELECT * FROM company_info"
        companyInfo = pd.read_sql(sql, self.conn)
        for idx in range(len(companyInfo)):
            self.codes[companyInfo['code'].values[idx]] = companyInfo['company'].values[idx]

    def getDailyPrice(self, code, startDate = None, endDate = None):
        """daily_price 테이블에서 읽어와서 데이터프레임으로 반환"""
        if startDate == None:
            oen_month_age = datetime.today() - timedelta(days=30)
            startDate = oen_month_age.strftime('%Y-%m-%d')
            endDate = datetime.today()
            print(startDate + ' : 시작일')

        code = self.find_code(code)

        if code == None:
            pass
        else:
            sql = "SELECT * FROM daily_price WHERE code = '{}' and date >= '{}' and date <= '{}'".format(code, startDate, endDate)
            df = pd.read_sql(sql, self.conn)
            df.index = df['date']
            return df

    def find_code(self, data):
        code_keys = list(self.codes.keys())
        code_value = list(self.codes.values())

        if data in code_keys:
            return data
        elif data in code_value:
            idx = code_value.index(data)
            code = code_keys[idx]
            return code
        else:
            print('없는 코드 : ' + data)


if __name__ == '__main__':
    day_data = MarketDB()
    df = day_data.getDailyPrice('삼성전자')
    print(df)

