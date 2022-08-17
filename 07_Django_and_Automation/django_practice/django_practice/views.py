
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from bs4 import BeautifulSoup
from urllib.request import urlopen

class main_views(APIView):
    def get_data(self, symbol):
        url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
        with urlopen(url) as doc:
            soup = BeautifulSoup(doc, "lxml", from_encoding="euc-kr")
            cur_price = soup.find('strong', id='_nowVal')  # ①
            cur_rate = soup.find('strong', id='_rate')  # ②
            stock = soup.find('title')  # ③
            stock_name = stock.text.split(':')[0].strip()  # ④
            return cur_price.text, cur_rate.text.strip(), stock_name

    def mainview(self, request):
        querydict = request.GET.copy()
        mylist = querydict.lists()  # ⑤
        rows = []
        total = 0

        for x in mylist:
            cur_price, cur_rate, stock_name = self.get_data(x[0])  # ⑥
            price = cur_price.replace(',', '')
            stock_count = format(int(x[1][0]), ',')  # ⑦
            sum = int(price) * int(x[1][0])
            stock_sum = format(sum, ',')
            rows.append([stock_name, x[0], cur_price, stock_count, cur_rate,
                stock_sum])  # ⑧
            total = total + int(price) * int(x[1][0])  # ⑨

        total_amount = format(total, ',')
        values = {'rows' : rows, 'total' : total_amount}  # ⑩
        return render(request, 'ch07_05_balance.html', values)  # ⑪
