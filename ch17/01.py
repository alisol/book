import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
df = web.DataReader("078930.KS", "yahoo", start, end)

con = sqlite3.connect("kospi.db") # 책에는 데이타베이스 경로가 있음.
df.to_sql('078930', con, if_exists='replace')

readed_df = pd.read_sql("SELECT * FROM '078930'", con, index_col = 'Date')
print(readed_df) # 책에는 이 출력문이 없음.
