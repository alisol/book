import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.ticker as ticker

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)

skhynix = web.DataReader("000660.KS", "yahoo", start, end)
#skhynix = skhynix[skhynix['Volume'] > 0] # 개정판에는 이 부분이 실행되도록 설정됨. 왜 주석처리한건가?

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
day_list = range(len(skhynix))

name_list = []
for day in skhynix.index:
    name_list.append(day.strftime('%d'))

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

mpl_finance.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')
plt.show()
