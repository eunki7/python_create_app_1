import sys
import io
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import simplejson as json

#tinyDB, simplejson

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 생성
db = TinyDB('c:/section5/databases/database.db',default_table='todos') #테이블명 지정안하면 default로 생성
db = TinyDB('c:/section5/databases/database.db',default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='todos')
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#테이블 데이터 삽입
users.insert({'name': 'kim', 'email': 'test@google.com'})
todos.insert({'name': 'homework', 'complete': False})

#테이블 데이터 전체 삽입1
with open('c:/section5/data/users.json','r') as infile:
    r = json.loads(infile.read())
    for p in r:
        users.insert(p)

#테이블 데이터 전체 삽입2
with open('c:/section5/data/todos.json','r') as infile:
    r = json.loads(infile.read())
    for p in r:
        todos.insert(p)

#전체 데이터 출력
print(users.all())
print(todos.all())

#테이블 목록 조회
print(db.tables())

#전체 데이터 삭제
users.purge()
todos.purge()

db.purge_table('users')
db.purge_table('todos')

db.purge_tables()

db.close()
