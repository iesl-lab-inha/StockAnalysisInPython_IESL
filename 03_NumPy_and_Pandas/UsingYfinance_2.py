from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

Hansol = pdr.get_data_yahoo('025750.KS', start = '2022-01-01') #한솔홈데코의 주가 검색
Hanjin = pdr.get_data_yahoo('180640.KS', start = '2022-01-01') #한진칼의 주가 검색

Hansol_dpc = (Hansol['Close'] - Hansol['Close'].shift(1))/Hansol['Close'].shift(1) * 100 #한솔홈데코의 일간변동률 계산
Hanjin_dpc = (Hanjin['Close']- Hanjin['Close'].shift(1))/Hanjin['Close'].shift(1) * 100 #핝진칼의 일간변동률 계산

Hansol_dpc_cp = ((100+Hansol_dpc)/100).cumprod()*100-100 #한솔홈데코의 일간변동률의 누적곱, 주식수익율 계산
Hanjin_dpc_cp= ((100+Hanjin_dpc)/100).cumprod()*100-100 #한진칼의 일간변동률의 누적곱, 주식수익율 계산

#1 1월1일부터의 주가 그래프
import matplotlib.pyplot as plt
plt.title("Hansol Home Deco VS Hanjin Kal (2022.01.01 ~ )")
plt.plot(Hansol.index, Hansol.Close, 'g--', label ="Hansol")
plt.plot(Hanjin.index, Hanjin.Close, 'r--', label ="Hanjin")
plt.grid(True)
plt.show()

#2 1월1일부터의 주식수익률 그래프
plt.title("Cumulative Product of Hansol Home Deco VS Hanjin Kal (2022.01.01 ~ )")
plt.plot(Hansol.index, Hansol_dpc_cp, 'g-', label="Hansol_CP")
plt.plot(Hanjin.index, Hanjin_dpc_cp, 'r-', label="Hanjin_CP")
plt.grid(True)
plt.ylabel('Change %')
plt.legend(loc='best')
plt.show()