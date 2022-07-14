Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> import matplotlib.pyplot as plt
>>> kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')
[*********************100%***********************]  1 of 1 completed
>>> window = 252
>>> peak = kospi['Adj Close'].rolling(window, min_periods=1).max()
>>> drawdown = kospi['Adj Close']/peak - 1.0
>>> max_dd = drawdown.rolling(window, min_periods=1).min()
>>> plt.figure(figsize=(9, 7))
<Figure size 900x700 with 0 Axes>
>>> plt.subplot(211)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000022CD5019520>
>>> kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid = True, legend = True)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000022CD5019520>
>>> plt.subplot(212)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000022CD735C790>
>>> drawdown.plot(c='blue', label='KOSPI DD', grid = True, legend = True)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000022CD735C790>
>>> max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000022CD735C790>
>>> plt.show()
>>> max_dd.min()
-0.5453665130144085
>>> max_dd[max_dd==-0.5453665130144085]
Date
2008-10-24   -0.545367
2008-10-27   -0.545367
2008-10-28   -0.545367
2008-10-29   -0.545367
2008-10-30   -0.545367
                ...   
2009-10-16   -0.545367
2009-10-19   -0.545367
2009-10-20   -0.545367
2009-10-21   -0.545367
2009-10-22   -0.545367
Name: Adj Close, Length: 252, dtype: float64
>>> 