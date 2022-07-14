Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> from scipy import stats
>>> import matplotlib.pylab as plt
>>> dow = pdr.get_data_yahoo('TLT', '2002-07-30')
[*********************100%***********************]  1 of 1 completed
>>> kospi = pdr.get_data_yahoo('^KS11', '2002-07-30')
[*********************100%***********************]  1 of 1 completed
>>> df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']})
>>> df = df.fillna(method = 'bfill')
>>> df = df.fillna(method = 'ffill')
>>> regr = stats.linregress(df.X, df.Y)
>>> regr_line = f'Y ={regr.slpe:.2f} * X + {regr.intercept:.2f}'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    regr_line = f'Y ={regr.slpe:.2f} * X + {regr.intercept:.2f}'
AttributeError: 'LinregressResult' object has no attribute 'slpe'
>>> regr_line = f'Y ={regr.slope:.2f} * X + {regr.intercept:.2f}'
>>> plt.figure(figsize=(7, 7))
<Figure size 700x700 with 0 Axes>
>>> plt.plot(df.X, df.Y, '.')

Warning (from warnings module):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\cbook\__init__.py", line 1402
    ndim = x[:, None].ndim
FutureWarning: Support for multi-dimensional indexing (e.g. `obj[:, None]`) is deprecated and will be removed in a future version.  Convert to a numpy array before indexing instead.

Warning (from warnings module):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 276
    x = x[:, np.newaxis]
FutureWarning: Support for multi-dimensional indexing (e.g. `obj[:, None]`) is deprecated and will be removed in a future version.  Convert to a numpy array before indexing instead.

Warning (from warnings module):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_base.py", line 278
    y = y[:, np.newaxis]
FutureWarning: Support for multi-dimensional indexing (e.g. `obj[:, None]`) is deprecated and will be removed in a future version.  Convert to a numpy array before indexing instead.
[<matplotlib.lines.Line2D object at 0x000001B6378382B0>]
>>> plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
[<matplotlib.lines.Line2D object at 0x000001B6378387C0>]
>>> plt.legend(['DOW x KOSPI', regr_line])
<matplotlib.legend.Legend object at 0x000001B637838670>
>>> plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
Text(0.5, 1.0, 'DOW x KOSPI (R = 0.74)')
>>> plt.xlabel('Dow Jones Industrial Average')
Text(0.5, 0, 'Dow Jones Industrial Average')
>>> plt.ylabel('KOSPI')
Text(0, 0.5, 'KOSPI')
>>> plt.show()
>>> 
================================ RESTART: Shell ================================
>>> import pandas as pd
>>> s1 = pd.Series([+10, -20, +30, -40, +50])
>>> s2 = pd.Series([+1, -2, +3, -4, +5])
>>> s3 = pd.Series([-10, +20, -30, +40, -50])
>>> df = pd.DataFrame({'S1' : s1, 'S2' : s2, 'S3' : s3})
>>> df
   S1  S2  S3
0  10   1 -10
1 -20  -2  20
2  30   3 -30
3 -40  -4  40
4  50   5 -50
>>> df.corr()
     S1   S2   S3
S1  1.0  1.0 -1.0
S2  1.0  1.0 -1.0
S3 -1.0 -1.0  1.0
>>> 