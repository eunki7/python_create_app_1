import sys
import io
from tinydb import TinyDB, Query

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 생성
db = TinyDB('c:/section5/databases/database.db')

#데이터 삽입
db.insert({'name': 'kim', 'email': 'test1@daum.net'})
db.insert_multiple([{'name': 'lee', 'email': 'test2@daum.net'},{'name': 'park', 'email': 'test3@daum.net'}]) #JsonArray 삽입

SQL = Query()

#데이터 수정
el = db.get(SQL.name == 'kim')

#id값 출력
print(el)
print(el.doc_id)

db.update({'email': 'test1@google.com'}, doc_ids=[3])
db.update({'email': 'test1@google.com'}, doc_ids=[1,2,3])

#데이터 수정 & 추가
db.upsert({'email': 'test1@naver.com', 'login': True}, SQL.name == 'kim')

#데이터 삭제
db.remove(doc_ids=[2,3])
db.remove(SQL.name == 'park')
#전체 조회
print(db.all())

#접속 종료
db.close()
