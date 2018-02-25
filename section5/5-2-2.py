import sys
import io
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 로드
db = TinyDB('c:/section5/databases/database.db')

#메모리 DB 로드
#db = TinyDB(storage=MemoryStorage)

#users, todos 테이블 선택
users = db.table('users')
todos = db.table('todos')

#users 테이블 출력
for item in users:
    print(item['username'], ' : ',item['phone'])

#todos 테이블 출력
for item in todos:
    print(item['title'], ' : ',item['completed'])

#연결 관계 출력(조건문)
for item in users:
    print('[',item['username'],']')
    for todo in todos:
        if todo['userId'] == item['id']:
            print(todo['title'])


#쿼리 객체 사용 조회
Users = Query()
Todos = Query()

user_3 = users.search(Users.id == 3) #>, <, >=, <=, ==
print(users.search(Users.id == 3))
print(user_3)

todo_t = todos.search(Todos.completed == True)
print(todos.search(Todos.completed == True))
print(todo_t)

#연결 관계 출력(쿼리)
for item in users:
    print('[',item['username'],']')
    user1 = todos.search(Todos.userId == item['id'])
    for todo in user1:
        print(todo)

#쿼리 객체 사용 수정
users.update({'username': 'kim'}, Users.id == 3)
print(users.search(Users.id == 3))

#쿼리 객체 사용 삭제
users.remove(Users.id == 3)
print(users.search(Users.id == 3))

#DB 전체 삭제
db.purge()

#DB 전체 출력
db.all()

#DB 커넥션 종료
db.close()
