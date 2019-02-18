import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

#조회 시작 날짜
start = datetime.datetime(2016, 2, 19)
#조회 마감 날짜
end = datetime.datetime(2016, 3, 4)

#Google API 금융 정보 호출
gs = web.DataReader('NASDAQ: GOOG', 'google')
#gs = web.DataReader('NASDAQ: GOOG', 'google', start, end)

#출력
print(gs.index)
print(gs['Open'])
print(gs.ix['2016-02-19'])
print(gs.describe())