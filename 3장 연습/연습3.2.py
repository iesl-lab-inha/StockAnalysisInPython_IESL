Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
>>> s
0    0.0
1    3.6
2    2.0
3    5.8
4    4.2
5    8.0
dtype: float64
>>> 
>>> s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
>>> s.index.name = 'MY_IDX'
>>> s
MY_IDX
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
dtype: float64
>>> s.name = 'MY_SERIES'
>>> s
MY_IDX
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
Name: MY_SERIES, dtype: float64
>>> s[5.9] = 5.5
>>> s
MY_IDX
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
Name: MY_SERIES, dtype: float64
>>> import warnings
>>> warnings.simplefilter(action='ignore', category=FutureWarning)
>>> ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
>>> s = s.append(ser)
>>> s
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
6.8    6.7
8.0    4.2
dtype: float64
>>> 
>>> s.index[-1]
8.0
>>> s.values[-1]
4.2
>>> s.loc[8.0]
4.2
>>> s.iloc[-1]
4.2
>>> s.values[:]
array([0. , 3.6, 2. , 5.8, 4.2, 8. , 5.5, 6.7, 4.2])
>>> s.iloc[:]
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
6.8    6.7
8.0    4.2
dtype: float64
>>> s.drop(8.0)
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
6.8    6.7
dtype: float64
>>> s.describe()
count    9.000000
mean     4.444444
std      2.430078
min      0.000000
25%      3.600000
50%      4.200000
75%      5.800000
max      8.000000
dtype: float64
>>> 
================================ RESTART: Shell ================================
>>> import pandas as pd
>>> s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])
>>> s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])
>>> s.index.name = 'MY_INDEX'
>>> s.name = 'MY_SERIES'
>>> 
>>> import matplotlib.pyplot as plt
>>> plt.title("ELLIOTT_WAVE")
Text(0.5, 1.0, 'ELLIOTT_WAVE')
>>> plt.plot(s,'bs--')
[<matplotlib.lines.Line2D object at 0x00000230A9B47EE0>]
>>> plt.xticks(s.index)
([<matplotlib.axis.XTick object at 0x00000230AAC5EAF0>, <matplotlib.axis.XTick object at 0x00000230AAC5EAC0>, <matplotlib.axis.XTick object at 0x00000230AAC5E3A0>, <matplotlib.axis.XTick object at 0x00000230AF0558E0>, <matplotlib.axis.XTick object at 0x00000230AF055E80>, <matplotlib.axis.XTick object at 0x00000230AF06D460>, <matplotlib.axis.XTick object at 0x00000230AF06DA00>, <matplotlib.axis.XTick object at 0x00000230AF06DFA0>, <matplotlib.axis.XTick object at 0x00000230AF072580>], <a list of 9 Text xticklabel objects>)
>>> plt.yticks(s.value)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    plt.yticks(s.value)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 5575, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value'
>>> plt.yticks(s.values)
([<matplotlib.axis.YTick object at 0x00000230AF02B460>, <matplotlib.axis.YTick object at 0x00000230AAC5EFA0>, <matplotlib.axis.YTick object at 0x00000230AAC5E7C0>, <matplotlib.axis.YTick object at 0x00000230AF0726A0>, <matplotlib.axis.YTick object at 0x00000230AF06D130>, <matplotlib.axis.YTick object at 0x00000230AFCDE130>, <matplotlib.axis.YTick object at 0x00000230AFCDE6D0>, <matplotlib.axis.YTick object at 0x00000230AFCDEC70>, <matplotlib.axis.YTick object at 0x00000230AFCE2250>], <a list of 9 Text yticklabel objects>)
>>> plt.grid(True)

>>> plt.show()
>>> 
