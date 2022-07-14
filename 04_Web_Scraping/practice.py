import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
# 4.4.3 맨 뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
print(html)



bs = BeautifulSoup(html, 'lxml')

#  html 맨뒤 버튼
#                 <td class="pgRR">
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=420"  >맨뒤
# 				<img src="https://ssl.pstatic.net/static/n/cmn/bu_pgarRR.gif" width="8" height="5" alt="" border="0">
# 				</a>
# 				</td>


pgrr = bs.find('td', class_='pgRR')             # 맨뒤버튼찾기
s = str(pgrr.a['href']).split('=')              # 맨뒤 버튼의 하이퍼링크 주소 가져오기 + page 숫자 앞 = 과 분리
last_page = s[-1]                               # 마지막페이지가 제일 뒤에 있음을 알 수 있음

# 4.4.4 전체 페이지 읽어오기
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1, int(last_page)+1):                     # 1 부터 마지막 페이지 까지
    url = '{}&page={}'.format(sise_url, page)               # URL 주소를 보면 마지막에 PAGE를 입력함
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text    # 그대로 HTML 가져옴

    df = df.append(pd.read_html(html, header=0)[0])         # 읽어온 값 뒤에다 붙이기
    print(pd.read_html(html, header=0)[0])


# '''
# <html lang="ko">
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
# <title>네이버 금융</title>
#
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/newstock.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/common.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/layout.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/main.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/newstock2.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/newstock3.css">
# <link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/css/world.css">
# </head>
# <body>
# <script language="JavaScript">
# function mouseOver(obj){
#   obj.style.backgroundColor="#f6f4e5";
# }
# function mouseOut(obj){
#   obj.style.backgroundColor="#ffffff";
# }
# </script>
# 				<h4 class="tlline2"><strong><span class="red03">일별</span>시세</strong></h4>
# 				<table cellspacing="0" class="type2">
# 				<tr>
# 				<th>날짜</th>
# 				<th>종가</th>
# 				<th>전일비</th>
# 				<th>시가</th>
# 				<th>고가</th>
# 				<th>저가</th>
# 				<th>거래량</th>
# 				</tr>
# 				<tr>
# 				<td colspan="7" height="8"></td>
# 				</tr>
#
#
#
# 				<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 				<td align="center"><span class="tah p10 gray03">2022.07.11</span></td>
# 				<td class="num"><span class="tah p11">186,000</span></td>
# 				<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				3,500
# 				</span>
# 			</td>
# 				<td class="num"><span class="tah p11">181,500</span></td>
# 				<td class="num"><span class="tah p11">187,500</span></td>
# 				<td class="num"><span class="tah p11">181,500</span></td>
# 				<td class="num"><span class="tah p11">341,446</span></td>
# 				</tr>
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.08</span></td>
# 					<td class="num"><span class="tah p11">182,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
# 				5,000
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">187,000</span></td>
# 					<td class="num"><span class="tah p11">187,000</span></td>
# 					<td class="num"><span class="tah p11">178,500</span></td>
# 					<td class="num"><span class="tah p11">755,595</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.07</span></td>
# 					<td class="num"><span class="tah p11">187,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				1,000
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">188,000</span></td>
# 					<td class="num"><span class="tah p11">189,000</span></td>
# 					<td class="num"><span class="tah p11">184,500</span></td>
# 					<td class="num"><span class="tah p11">369,149</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.06</span></td>
# 					<td class="num"><span class="tah p11">186,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				3,500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">181,500</span></td>
# 					<td class="num"><span class="tah p11">190,000</span></td>
# 					<td class="num"><span class="tah p11">181,500</span></td>
# 					<td class="num"><span class="tah p11">892,324</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.05</span></td>
# 					<td class="num"><span class="tah p11">183,000</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				3,500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">180,000</span></td>
# 					<td class="num"><span class="tah p11">183,000</span></td>
# 					<td class="num"><span class="tah p11">177,500</span></td>
# 					<td class="num"><span class="tah p11">453,142</span></td>
# 					</tr>
#
#
#
#
#
#
# 				<tr>
# 				<td colspan="7" height="8"></td>
# 				</tr>
# 				<tr>
# 				<td colspan="7" height="1" bgcolor="#e1e1e1"></td>
# 				</tr>
# 				<tr>
# 				<td colspan="7" height="8"></td>
# 				</tr>
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.04</span></td>
# 					<td class="num"><span class="tah p11">179,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">179,000</span></td>
# 					<td class="num"><span class="tah p11">181,500</span></td>
# 					<td class="num"><span class="tah p11">177,000</span></td>
# 					<td class="num"><span class="tah p11">422,485</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.07.01</span></td>
# 					<td class="num"><span class="tah p11">179,000</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">180,500</span></td>
# 					<td class="num"><span class="tah p11">183,000</span></td>
# 					<td class="num"><span class="tah p11">174,000</span></td>
# 					<td class="num"><span class="tah p11">527,545</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.06.30</span></td>
# 					<td class="num"><span class="tah p11">178,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				2,500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">175,500</span></td>
# 					<td class="num"><span class="tah p11">184,000</span></td>
# 					<td class="num"><span class="tah p11">175,500</span></td>
# 					<td class="num"><span class="tah p11">803,073</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.06.29</span></td>
# 					<td class="num"><span class="tah p11">176,000</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
# 				1,500
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">174,500</span></td>
# 					<td class="num"><span class="tah p11">178,000</span></td>
# 					<td class="num"><span class="tah p11">173,000</span></td>
# 					<td class="num"><span class="tah p11">410,355</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
# 					<tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
# 					<td align="center"><span class="tah p10 gray03">2022.06.28</span></td>
# 					<td class="num"><span class="tah p11">174,500</span></td>
# 					<td class="num">
# 				<img src="https://ssl.pstatic.net/imgstock/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
# 				1,000
# 				</span>
# 			</td>
# 					<td class="num"><span class="tah p11">174,500</span></td>
# 					<td class="num"><span class="tah p11">176,000</span></td>
# 					<td class="num"><span class="tah p11">168,000</span></td>
# 					<td class="num"><span class="tah p11">568,410</span></td>
# 					</tr>
#
#
#
#
#
#
#
#
#
#
#
#
#
# 				<tr>
# 				<td colspan="7" height="8"></td>
# 				</tr>
# 				</table>
# 				<!--- 페이지 네비게이션 시작--->
# 				<table summary="페이지 네비게이션 리스트" class="Nnavi" align="center">
# 				<caption>페이지 네비게이션</caption>
# 				<tr>
#
#
#
#                 <td class="on">
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=1"  >1</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=2"  >2</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=3"  >3</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=4"  >4</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=5"  >5</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=6"  >6</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=7"  >7</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=8"  >8</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=9"  >9</a>
# 				</td>
# <td>
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=10"  >10</a>
# 				</td>
#
#                 <td class="pgR">
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=11"  >
# 				다음<img src="https://ssl.pstatic.net/static/n/cmn/bu_pgarR.gif" width="3" height="5" alt="" border="0">
# 				</a>
# 				</td>
#
#                 <td class="pgRR">
# 				<a href="/item/sise_day.nhn?code=068270&amp;page=420"  >맨뒤
# 				<img src="https://ssl.pstatic.net/static/n/cmn/bu_pgarRR.gif" width="8" height="5" alt="" border="0">
# 				</a>
# 				</td>
#
#
# 				</tr>
# 				</table>
# 				<!--- 페이지 네비게이션 끝--->
#
#
# 	<script type="text/javascript" src="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/js/jindo.min.ns.1.5.3.euckr.js"></script>
# 	<script type="text/javascript" src="https://ssl.pstatic.net/imgstock/static.pc/20220615142521/js/lcslog.js"></script>
# 	<script type="text/javascript">
#         ;(function(){
#             var eventType = "onpageshow" in window ? "pageshow" : "load";
#             jindo.$Fn(function(){
#                 lcs_do();
#             }).attach(window, eventType);
#         })();
# 	</script>
#
# </body>
#
# '''