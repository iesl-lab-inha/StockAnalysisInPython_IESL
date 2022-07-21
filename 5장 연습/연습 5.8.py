def read_naver(self, code, company, pages_to_fetch):
    """네이버에서 주식 시세를 읽어서 데이터프레임으로 반환"""
    try:
        url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
        with urlopen(url) as doc:
            if doc is None:
                return None
            html = BeautifulSoup(doc, "lxml")
            pgrr = html.find("td", class_="pgRR")
            if pgrr is None:
                return None
            s = str(pgrr.a["href"]).split('=')
            lastpage = s[-1]
        df = pd.DataFrame()
        pages = min(int(lastpage), pages_to_fetch)
        for page in range(1, pages + 1):
            pg_url = '{}&page={}'.format(url, page)
            df = df.append(pd.read_html(pg_url, header=0)[0])
            tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
            print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.
                  format(tmnow, company, code, page, pages), end="\r")
        df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff'
            , '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
        df['date'] = df['date'].replace('.', '-')
        df = df.dropna()
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
                                                                     'diff', 'open', 'high', 'low', 'volume']].astype(
            int)
        df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
    except Exception as e:
        print('Exception occured :', str(e))
        return None
    return df

    def replace_into_db(self, df, num, code, company):
        """네이버에서 읽어온 주식 시세를 DB에 REPLACE"""
        with self.conn.cursor() as curs:
            for r in df.itertuples():
                sql = f"REPLACE INTO daily_price VALUES ('{code}', "\
                    f"'{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, "\
                    f"{r.diff}, {r.volume})"
                curs.execute(sql)
            self.conn.commit()
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_'\
                'price [OK]'.format(datetime.now().strftime('%Y-%m-%d'\
                ' %H:%M'), num+1, company, code, len(df)))