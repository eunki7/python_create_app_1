import threading

#쓰레드 실행 - 함수형
def thread_run():
    print('Thread running - F')

def thread_run_msg(msg):
    print('Thread running - F : ', msg)

for i in range(1000):
    t = threading.Thread(target=thread_run)
    t1 = threading.Thread(target=thread_run_msg, args=('service',))
    #쓰레드 시작
    t.start()
    t1.start()
