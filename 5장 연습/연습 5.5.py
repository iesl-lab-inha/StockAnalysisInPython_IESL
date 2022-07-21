import pandas as pd
class DBUpdater:
    def read_krx_code(self):
        def read_krx_code(self):
            """KRX로부터 상장기업 목록 파일을 읽어와서 데이터프레임으로 반환"""
            url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=' \
                  'download&searchType=13'
            krx = pd.read_html(url, header=0)[0]
            krx = krx[['종목코드', '회사명']]
            krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
            krx.code = krx.code.map('{:06d}'.format)
            return krx