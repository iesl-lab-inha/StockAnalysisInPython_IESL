Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]
>>> df = df.sort_values(by='종목코드')
>>> df
             회사명    종목코드  ...                              홈페이지     지역
32          동화약품      20  ...         http://www.dong-wha.co.kr  서울특별시
337        KR모터스      40  ...           http://www.krmotors.com   경상남도
1571          경방      50  ...        http://www.kyungbang.co.kr  서울특별시
666        메리츠화재      60  ...         http://www.meritzfire.com  서울특별시
677        삼양홀딩스      70  ...            http://www.samyang.com  서울특별시
...          ...     ...  ...                               ...    ...
1660         JTC  950170  ...   http://www.groupjtc.com/korean/     일본
2002         미투젠  950190  ...             http://www.me2zen.com     홍콩
2024         소마젠  950200  ...               http://psomagen.com     미국
1936  프레스티지바이오파마  950210  ...  http://www.prestigebiopharma.com   싱가포르
1369       네오이뮨텍  950220  ...        http://neoimmunetech.co.kr     미국

[2509 rows x 9 columns]
>>> 