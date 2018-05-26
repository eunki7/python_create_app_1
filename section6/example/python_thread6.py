#일정 시간 간격으로 크롤링 및 기타 반복 작업 가능한 예제
import time
import threading

def thread_run():
    print('=====',time.ctime(),'=====')
    for i in range(1,50001):
        #개발 하고자 하는 코드
        print('Thread running - ', i)

    threading.Timer(2.5, thread_run).start()

thread_run()
#threading.Timer(2, thread_run).start() : 메인에서 실행하면 1회 실행
