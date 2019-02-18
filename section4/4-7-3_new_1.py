import datetime
import FinanceDataReader as fdr

#조회 시작 날짜
start = datetime.datetime(2016, 2, 19)
#조회 마감 날짜
end = datetime.datetime(2016, 3, 4)

# 한국거래소 상장종목 전체
df_krx = fdr.StockListing('KRX')

# 리스트 10개 출력
print(df_krx.head(10))

#출력
print(df_krx.index)
print(df_krx['Symbol'])
print(df_krx.ix[0])
print(df_krx.describe())

#미국주식 APPLE 금융 정보 호출
df_app = fdr.DataReader('AAPL', start, end)
print(df_app.head(10))
print(df_app.ix['2016-02-25'])
print(df_app.describe())

#미국주식 아마존 금융 정보 호출
df_amz = fdr.DataReader('AMZN', start, end)
print(df_amz.head(10))
print(df_amz.ix['2016-02-25'])
print(df_amz.describe())

#미국주식 구글 금융 정보 호출
df_goog = fdr.DataReader('GOOG', start, end)
print(df_goog.head(10))
print(df_goog.ix['2016-02-25'])
print(df_goog.describe())