import matplotlib.pyplot as plt

# 마지막에 색깔 지정
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# X값 최소, X값 최대, Y값 최소, Y값 최대
plt.axis([0, 6, 0, 20])
plt.show()

import numpy as np

# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)

# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()