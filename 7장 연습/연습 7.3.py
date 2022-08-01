from datetime import datetime
import yfinance as yf

import backtrader as bt

class MyStrategy(bt.Strategy):  # ①
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)  # ②
    def next(self):  # ③
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

cerebro = bt.Cerebro()  # ④
cerebro.addstrategy(MyStrategy)
data = bt.feeds.PandasData(dataname=yf.download('036570.KS', '2017-01-01', '2019-12-01', auto_adjust=True))
cerebro.adddata(data)
cerebro.broker.setcash(10000000)  # ⑥
cerebro.addsizer(bt.sizers.SizerFix, stake=30)  # ⑦

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()  # ⑧
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot()  # ⑨