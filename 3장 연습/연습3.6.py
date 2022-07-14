Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> 
>>> dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(9, 5))
<Figure size 900x500 with 0 Axes>
>>> plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial')

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
[<matplotlib.lines.Line2D object at 0x000001986D0A25B0>]
>>> plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
[<matplotlib.lines.Line2D object at 0x000001986F2B92B0>]
>>> plt.grid(True)
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x000001986F2B96A0>
>>> plt.show()
>>> 
>>> d = (dow.Close / dow.Close.loc['2000-01-04'])*100
>>> k = (kospi.Close / kospi.Close.loc['2000=01-04']) * 100
Traceback (most recent call last):
  File "pandas\_libs\tslibs\parsing.pyx", line 362, in pandas._libs.tslibs.parsing.parse_datetime_string_with_reso
  File "pandas\_libs\tslibs\parsing.pyx", line 570, in pandas._libs.tslibs.parsing.dateutil_parse
ValueError: Unknown datetime string format, unable to parse: 2000=01-04

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\datetimes.py", line 644, in get_loc
    parsed, reso = self._parse_with_reso(key)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\datetimelike.py", line 231, in _parse_with_reso
    parsed, reso_str = parsing.parse_time_string(label, self.freq)
  File "pandas\_libs\tslibs\parsing.pyx", line 321, in pandas._libs.tslibs.parsing.parse_time_string
  File "pandas\_libs\tslibs\parsing.pyx", line 367, in pandas._libs.tslibs.parsing.parse_datetime_string_with_reso
pandas._libs.tslibs.parsing.DateParseError: Unknown datetime string format, unable to parse: 2000=01-04

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    k = (kospi.Close / kospi.Close.loc['2000=01-04']) * 100
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 967, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 1202, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 1153, in _get_label
    return self.obj.xs(label, axis=axis)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 3864, in xs
    loc = index.get_loc(key)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\datetimes.py", line 646, in get_loc
    raise KeyError(key) from err
KeyError: '2000=01-04'
>>> k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(9, 5))
<Figure size 900x500 with 0 Axes>
>>> plt.plot(d.index, d, 'r--', label='Dow Jones Industrial')
[<matplotlib.lines.Line2D object at 0x000001986D082DC0>]
>>> plt.plot(k.index, k, 'b', label='KOSPI')
[<matplotlib.lines.Line2D object at 0x000001987191E580>]
>>> plt.grid(True)
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x00000198719102B0>
>>> plt.show()
>>> 
>>> len(dow); len(kospi)
5667
5556
>>> plt.scatter(dow, kospi, marker='.')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    plt.scatter(dow, kospi, marker='.')
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\pyplot.py", line 2836, in scatter
    __ret = gca().scatter(
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\__init__.py", line 1599, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\matplotlib\axes\_axes.py", line 4443, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> 
>>> df = pd.DataFrame({'DOW' : dow['Close'], 'KOSPI' : kospi['Close']})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df = pd.DataFrame({'DOW' : dow['Close'], 'KOSPI' : kospi['Close']})
NameError: name 'pd' is not defined
>>> import pandas as pd
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> df = pd.DataFrame({'DOW': dow['Close']. 'KOSPI': kospi['Close']})
SyntaxError: invalid syntax
>>> df = pd.DataFrame({'DOW' : dow['Close'], 'KOSPI' : kospi['Close']})
>>> df
                     DOW        KOSPI
Date                                 
2000-01-03  11357.509766          NaN
2000-01-04  10997.929688  1059.040039
2000-01-05  11122.650391   986.309998
2000-01-06  11253.259766   960.789978
2000-01-07  11522.559570   948.650024
...                  ...          ...
2022-07-07  31384.550781  2334.270020
2022-07-08  31338.150391  2350.610107
2022-07-11  31173.839844  2340.270020
2022-07-12  30981.330078  2317.760010
2022-07-13           NaN  2328.610107

[5842 rows x 2 columns]
>>> plt.scatter(df['DOW'], df['KOSPI'], marker='.')
<matplotlib.collections.PathCollection object at 0x00000198720FAD00>
>>> dtype('float64').
SyntaxError: invalid syntax
>>> df = df.fillna(method='bfill')
>>> df
                     DOW        KOSPI
Date                                 
2000-01-03  11357.509766  1059.040039
2000-01-04  10997.929688  1059.040039
2000-01-05  11122.650391   986.309998
2000-01-06  11253.259766   960.789978
2000-01-07  11522.559570   948.650024
...                  ...          ...
2022-07-07  31384.550781  2334.270020
2022-07-08  31338.150391  2350.610107
2022-07-11  31173.839844  2340.270020
2022-07-12  30981.330078  2317.760010
2022-07-13           NaN  2328.610107

[5842 rows x 2 columns]
>>> import pandas as pd
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> kospi = pdr.get_data_yahoo('KS11', '2000-01-04')
[*********************100%***********************]  1 of 1 completed

1 Failed download:
- KS11: No data found, symbol may be delisted
>>> kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
>>> df = df.fillna(method='bfill')
>>> df = df.fillna(method='ffill')
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(7, 7))
<Figure size 700x700 with 0 Axes>
>>> plt.scatter(df['DOW'], df['KOSPI'], marker='.')
<matplotlib.collections.PathCollection object at 0x000001987226EA60>
>>> plt.xlabel('DOW Jones Industrial Average')
Text(0.5, 0, 'DOW Jones Industrial Average')
>>> plt.ylabel('KOSPI')
Text(0, 0.5, 'KOSPI')
>>> plt.show()
>>> 
>>> from scipy import stats
>>> regr = stats.linregress(df['DOW'], df['KOSPI'])
>>> regr
LinregressResult(slope=0.07447336829018966, intercept=488.81010251529483, rvalue=0.8254659268818209, pvalue=0.0, stderr=0.0006663806828263138, intercept_stderr=11.72398674525938)
>>> df.corr()
            DOW     KOSPI
DOW    1.000000  0.825466
KOSPI  0.825466  1.000000
>>> df['DOW'].corr(df['KOSPI'])
0.8254659268818209
>>> r_value = df['DOW'].corr(df['KOSPI'])
>>> r_value
0.8254659268818209
>>> r_squared = r_value ** 2
>>> r_squared
0.6813939964428636
>>> 
============================================================================== RESTART: Shell =============================================================================
>>> import pandas as pd
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> from scipy import stats
>>> import matplotlib.pylab as plt
>>> dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
[*********************100%***********************]  1 of 1 completed
>>> df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']})
>>> df = df.fillna(method = 'bfill')
>>> df = df.fillna(method = 'ffill')
>>> regr = stats.linregress(df.X, df.Y)
>>> regr_line = f'Y ={regr.slpe:.2f} * X + {regr.intercept:.2f}'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
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
[<matplotlib.lines.Line2D object at 0x000001BD24805310>]
>>> plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
[<matplotlib.lines.Line2D object at 0x000001BD24805820>]
>>> plt.legend(['DOW x KOSPI', regr_line])
<matplotlib.legend.Legend object at 0x000001BD248056D0>
>>> plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
Text(0.5, 1.0, 'DOW x KOSPI (R = 0.83)')
>>> plt.xlabel('Dow Jones Industrial Average')
Text(0.5, 0, 'Dow Jones Industrial Average')
>>> plt.ylabel('KOSPI')
Text(0, 0.5, 'KOSPI')
>>> plt.show()
>>> 