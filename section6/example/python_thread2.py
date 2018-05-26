import threading

#쓰레드 실행 - 클래스 형
class Thread_Run(threading.Thread):
    def run(self):
        print('Thread running - C')

for i in range(1000):
    t = Thread_Run()
    #쓰레드 시작
    t.start()
