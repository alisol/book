import pandas_datareader.data as web
# import datetime
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

# data
yf.pdr_override()
# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2016, 3, 19)
# data = web.DataReader("AAPL", "yahoo", start, end)
data = web.get_data_yahoo("AAPL", start='2010-01-01", end="2019-01-01")

# data = data[['Adj Close']]
data = data[['Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()
