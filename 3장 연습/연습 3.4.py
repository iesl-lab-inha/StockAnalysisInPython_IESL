Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> sec.head(10)
               Open     High      Low    Close     Adj Close    Volume
Date                                                                  
2018-05-04  53000.0  53900.0  51800.0  51900.0  45953.542969  39565391
2018-05-08  52600.0  53200.0  51900.0  52600.0  46573.339844  23104720
2018-05-09  52600.0  52800.0  50900.0  50900.0  45068.109375  16128305
2018-05-10  51700.0  51700.0  50600.0  51600.0  45687.914062  13905263
2018-05-11  52000.0  52200.0  51200.0  51300.0  45422.285156  10314997
2018-05-14  51000.0  51100.0  49900.0  50100.0  44359.765625  14909272
2018-05-15  50200.0  50400.0  49100.0  49200.0  43562.890625  18709146
2018-05-16  49200.0  50200.0  49150.0  49850.0  44138.417969  15918683
2018-05-17  50300.0  50500.0  49400.0  49400.0  43739.976562  10365440
2018-05-18  49900.0  49900.0  49350.0  49500.0  43828.519531   6706570
>>> tmp_msft = msft.drop(columns='Volume')
>>> tmp_msft.tail()
                  Open        High         Low       Close   Adj Close
Date                                                                  
2022-07-06  263.750000  267.989990  262.399994  266.209991  266.209991
2022-07-07  265.119995  269.059998  265.019989  268.399994  268.399994
2022-07-08  264.790009  268.100006  263.290009  267.660004  267.660004
2022-07-11  265.649994  266.529999  262.179993  264.510010  264.510010
2022-07-12  265.880005  265.940002  252.039993  253.669998  253.669998
>>> 
>>> sec.index
DatetimeIndex(['2018-05-04', '2018-05-08', '2018-05-09', '2018-05-10',
               '2018-05-11', '2018-05-14', '2018-05-15', '2018-05-16',
               '2018-05-17', '2018-05-18',
               ...
               '2022-06-30', '2022-07-01', '2022-07-04', '2022-07-05',
               '2022-07-06', '2022-07-07', '2022-07-08', '2022-07-11',
               '2022-07-12', '2022-07-13'],
              dtype='datetime64[ns]', name='Date', length=1030, freq=None)
>>> sec.columns
Index(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], dtype='object')
>>> 
>>> 
================================ RESTART: Shell ================================
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
ms
>>> msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> import matplotlib.pyplot as plt
>>> plt.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')

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
[<matplotlib.lines.Line2D object at 0x0000026FA2686580>]
>>> plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
[<matplotlib.lines.Line2D object at 0x0000026FA4AE0280>]
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x0000026FA4AE0700>
>>> plt.show()
>>> 
================================ RESTART: Shell ================================
>>> type(sec['Close])
	 
SyntaxError: EOL while scanning string literal
>>> 
================================ RESTART: Shell ================================
>>> type(sec['Close'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type(sec['Close'])
NameError: name 'sec' is not defined
>>> 
================================ RESTART: Shell ================================
>>> from pandas_datareader import data as pdr
>>> 
================================ RESTART: Shell ================================
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> import matplotlib.pyplot as plt
>>> plt.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')

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
[<matplotlib.lines.Line2D object at 0x000001C5B7176550>]
>>> plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
[<matplotlib.lines.Line2D object at 0x000001C5B963C2E0>]
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x000001C5B963C670>
>>> plt.show()
>>> type(sec['Close'])
<class 'pandas.core.series.Series'>
>>> sec['Close']
Date
2018-05-04    51900.0
2018-05-08    52600.0
2018-05-09    50900.0
2018-05-10    51600.0
2018-05-11    51300.0
               ...   
2022-07-07    58200.0
2022-07-08    58700.0
2022-07-11    58800.0
2022-07-12    58100.0
2022-07-13    58000.0
Name: Close, Length: 1030, dtype: float64
>>> sec['Close'].shift(1)
Date
2018-05-04        NaN
2018-05-08    51900.0
2018-05-09    52600.0
2018-05-10    50900.0
2018-05-11    51600.0
               ...   
2022-07-07    56400.0
2022-07-08    58200.0
2022-07-11    58700.0
2022-07-12    58800.0
2022-07-13    58100.0
Name: Close, Length: 1030, dtype: float64
>>> sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
>>> sec_dpc.head
<bound method NDFrame.head of Date
2018-05-04         NaN
2018-05-08    1.348748
2018-05-09   -3.231939
2018-05-10    1.375246
2018-05-11   -0.581395
                ...   
2022-07-07    3.191489
2022-07-08    0.859107
2022-07-11    0.170358
2022-07-12   -1.190476
2022-07-13   -0.172117
Name: Close, Length: 1030, dtype: float64>
>>> sec_dpc.iloc[0] = 0
>>> sec_dpc.head()
Date
2018-05-04    0.000000
2018-05-08    1.348748
2018-05-09   -3.231939
2018-05-10    1.375246
2018-05-11   -0.581395
Name: Close, dtype: float64
>>> import matplotlib.pyplot as plt
>>> sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
>>> sec_dpc.iloc[0] = 0
>>> plt.hist(sec_dpc, bins = 18)
(array([  2.,   3.,  11.,  26.,  79., 169., 287., 242., 123.,  46.,  23.,
        10.,   6.,   1.,   1.,   0.,   0.,   1.]), array([-6.3876652 , -5.45109556, -4.51452593, -3.57795629, -2.64138666,
       -1.70481702, -0.76824739,  0.16832225,  1.10489188,  2.04146152,
        2.97803115,  3.91460079,  4.85117042,  5.78774006,  6.72430969,
        7.66087933,  8.59744896,  9.5340186 , 10.47058824]), <a list of 18 Patch objects>)
>>> plt.grid(True)
>>> plt.show
<function show at 0x000001C5B71159D0>
>>> sec_dpc.describe()
count    1030.000000
mean        0.023857
std         1.621055
min        -6.387665
25%        -0.967061
50%         0.000000
75%         0.858922
max        10.470588
Name: Close, dtype: float64
>>> sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100
>>> sec_dpc_cp
Date
2018-05-04     0.000000
2018-05-08     1.348748
2018-05-09    -1.926782
2018-05-10    -0.578035
2018-05-11    -1.156069
                ...    
2022-07-07    12.138728
2022-07-08    13.102119
2022-07-11    13.294798
2022-07-12    11.946050
2022-07-13    11.753372
Name: Close, Length: 1030, dtype: float64
>>> 
================================ RESTART: Shell ================================
>>> from pandas_datareader import data as pdr
>>> import yfinance as yf
>>> yf.pdr_override()
>>> sec = pdf.get_data_yahoo('005930.KS', start='2018-05-04')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sec = pdf.get_data_yahoo('005930.KS', start='2018-05-04')
NameError: name 'pdf' is not defined
>>> sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
>>> sec_dpc.iloc[0] = 0
>>> sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100
>>> 
>>> msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
[*********************100%***********************]  1 of 1 completed
>>> msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
>>> msft_dpc.iloc[0] = 0
>>> msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100 - 100
>>> 
>>> import matplotlib.pyplot as plt
>>> plt.plot(sec.index, sec_dpc_cp, 'b', label = 'Samsung Electronics')

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
[<matplotlib.lines.Line2D object at 0x00000245170828B0>]
>>> plt.plot(msft.index, msft_dpc_cp, 'r--', label = 'Microsoft')
[<matplotlib.lines.Line2D object at 0x00000245170824C0>]
>>> plt.ylabel('Change %')
Text(0, 0.5, 'Change %')
>>> plt.grid(True)
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x00000245170C7BB0>
>>> plt.show()
>>> 