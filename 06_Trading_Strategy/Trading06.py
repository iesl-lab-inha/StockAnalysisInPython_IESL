import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2018-04-23', '2022-07-25')['close']

print(df); print('\n')

daily_ret = df.pct_change()
print(daily_ret)
annual_ret = daily_ret.mean()*252
print(annual_ret)
daily_cov = daily_ret.cov()
print(daily_cov)
annual_cov = daily_cov*252
print(annual_cov)

port_ret = []
port_risk = []
port_weights = []
sharpe_ratio = []

#포트폴리오 제작
for _ in range(20000):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)

    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns' : port_ret, 'Risk' : port_risk, 'Sharpe' : sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weights[i] for weight in port_weights]
df2 = pd.DataFrame(portfolio)
df2 = df2[['Returns', 'Risk', 'Sharpe']+ [s for s in stocks]]

print(df2); print('\n')

max_sharpe = df2.loc[df2['Sharpe'] == df2['Sharpe'].max()]
min_risk = df2.loc[df2['Risk'] == df2['Risk'].min()]

df2.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap = 'viridis', edgecolors='k', figsize=(11,7), grid=True)
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.title('Portfolio Optimization')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()