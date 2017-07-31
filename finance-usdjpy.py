import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(1960, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('DEXJPUS', 'fred', start, end)
print(df.head(6))

df.plot()
plt.show()
