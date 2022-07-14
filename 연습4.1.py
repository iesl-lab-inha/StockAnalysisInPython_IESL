Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> krx_list = pd.read_html('C:/상장법인목록.xls')
>>> krx_list[0]
              회사명    종목코드  ...                          홈페이지     지역
0     대신밸런스제12호스팩  426670  ...                           NaN    NaN
1           영창케미칼  112290  ...      http://www.ycchem.co.kr/   경상북도
2         코난테크놀로지  402030  ...          http://konantech.com  서울특별시
3            넥스트칩  396270  ...      http://www.nextchip.com/    경기도
4          삼성스팩6호  425290  ...                           NaN  서울특별시
...           ...     ...  ...                           ...    ...
2504       CJ대한통운     120  ...    http://www.cjlogistics.com  서울특별시
2505        메리츠화재      60  ...     http://www.meritzfire.com  서울특별시
2506           경방      50  ...    http://www.kyungbang.co.kr  서울특별시
2507        유수홀딩스     700  ...  http://www.eusu-holdings.com  서울특별시
2508     한진중공업홀딩스    3480  ...  http://www.hhic-holdings.com    경기도

[2509 rows x 9 columns]
>>> krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
>>> krx_list[0]
              회사명    종목코드  ...                          홈페이지     지역
0     대신밸런스제12호스팩  426670  ...                           NaN    NaN
1           영창케미칼  112290  ...      http://www.ycchem.co.kr/   경상북도
2         코난테크놀로지  402030  ...          http://konantech.com  서울특별시
3            넥스트칩  396270  ...      http://www.nextchip.com/    경기도
4          삼성스팩6호  425290  ...                           NaN  서울특별시
...           ...     ...  ...                           ...    ...
2504       CJ대한통운  000120  ...    http://www.cjlogistics.com  서울특별시
2505        메리츠화재  000060  ...     http://www.meritzfire.com  서울특별시
2506           경방  000050  ...    http://www.kyungbang.co.kr  서울특별시
2507        유수홀딩스  000700  ...  http://www.eusu-holdings.com  서울특별시
2508     한진중공업홀딩스  003480  ...  http://www.hhic-holdings.com    경기도

[2509 rows x 9 columns]
