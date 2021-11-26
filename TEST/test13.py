import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.show()
# #创建包含时间序列的数据
# df = pd.DataFrame(np.random.randn(8,4),index=pd.date_range('2/1/2020',periods=8), columns=list('ABCD'))
# df.plot()
# plt.show()
#
# df = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
# #或使用df.plot(kind="bar")
# df.plot.bar()
# plt.show()


df = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
# df.plot(kind="bar",stacked=False)
#或者使用df.plot.bar(stacked="True")
df.plot(kind='area')
plt.show()

