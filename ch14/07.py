import pandas_datareader.data as web
# import datetime
import fix_yahoo_finance as yf #개정판
from zipline.api import order, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.finance import commission  #개정판
# from zipline.api import set_commission, commission
from zipline.utils.factory import create_simulation_parameters
# import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.float_format', '{:.3f}'.format)   #개정판

yf.pdr_override()  #개정판

# start = datetime.datetime(2016, 1, 1)
# end = datetime.datetime(2016, 1, 31)
# data = web.DataReader("078930.KS", "yahoo", start, end) #개정판
data = web.get_data_yahoo("078930.KS", start="2019-01-02", end="2019-01-25") #개정판

data = data[['Adj Close']]
data.columns = ['GS']
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('GS')
    set_commission(commission.PerDollar(cost=0.00165))

def handle_data(context, data):
    #order_target(context.sym, 1)
    order(context.sym, 1)

algo = TradingAlgorithm(sim_params=create_simulation_parameters(capital_base=100000000), initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result[['starting_cash', 'ending_cash', 'ending_value']])

