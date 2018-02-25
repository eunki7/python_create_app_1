import sys
import io
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 로드
db = TinyDB('c:/section5/databases/database.db')

#users, todos 테이블 선택
users = db.table('users')
todos = db.table('todos')

#쿼리 객체 사용 조회
Users = Query()
Todos = Query()

#Users 여러가지 조회 방법
user_3 = users.search(Users.id == 3) #>, <, >=, <=, ==
print('result_u',users.search(Users.id == 3))
print('result_u',users.search(Users['id'] == 3))
print('result_u',users.search(where('id') == 3))
print('result_u',users.search(Query()['id'] == 3))
print('result_u',users.search(where('address')['zipcode'] == '59590-4157'))
print('result_u',users.search(where('address').zipcode == '59590-4157'))
print('result_u',user_3)

#Todos 여러가지 조회 방법
todo_t = todos.search(Todos.completed == True)
print('result_t',todos.search(Todos.completed == True))
print('result_t',todos.search(Todos['completed'] == True))
print('result_t',todos.search(where('completed') == True))
print('result_t',todos.search(Query()['completed'] == True))
print('result_t',todo_t)

#고급 쿼리
print('exist1',users.search(Users.email.exists()))
print('exist2',users.search(Users['email'].exists()))

#정규표현식
print('matches',users.search(Users.username.matches('[aZ]*')))

#NOT
print('negate',users.search(~(Users.username == 'Moriah.Stanton')))

#OR
print('or',users.search((Users.username == 'Moriah.Stanton') | (Users.username == 'Samantha')))

#AND
print('and',users.search((Users.username == 'Moriah.Stanton') & (Users.id == 10)))

#기타 함수
print('len',len(users))
print('get',users.get(Users.username == 'Moriah.Stanton'))
print('contains',users.contains(Users.username == 'Moriah.Stanton'))
print('count',users.count(Users.username == 'Moriah.Stanton'))

#DB 커넥션 종료
db.close()
