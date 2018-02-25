import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

#조회 시작 날짜
start = datetime.datetime(2018, 2, 1)
#조회 마감 날짜
end = datetime.datetime(2018, 2, 17)

#네이버 주식 정보 조회
gs_naver = web.DataReader('KRX: 035420', 'google', start, end) #네이버
#다음카카오 주식 정보 조회
gs_daum = web.DataReader('KRX: 035720', 'google', start, end) #다음

#출력
print(gs_naver)
print(gs_daum)

#차트 윈도우 제목
fig = plt.figure('Charts Test')
#차트 사이즈 지정
fig.set_size_inches(10, 6, forward=True)

#차트 설정1
plt.plot(gs_naver.index, gs_naver['Close'], 'b', label="Naver")
#차트 설정2
plt.plot(gs_daum.index, gs_daum['Close'], 'r', label="Daum")

#범례 위치
plt.legend(loc='upper left')
#차트 제목
plt.title('Naver & Daum')

#x축 레이블
plt.xlabel('Date')
#y축 레이블
plt.ylabel('Close')

#차트 실행
plt.show()
