import sqlite3
import simplejson as json

#DB생성(파일)
conn = sqlite3.connect('C:/Django/workspace/python-class1/section5/database/sqlite.db')

#Cursor연결
c = conn.cursor()

#데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))

#데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'goodboy', 'id': 3})

#데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('cuteboy', 5))

#중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

#데이터 삭제1
c.execute("DELETE FROM users WHERE id = ?", (7,))

#데이터 삭제2
c.execute("DELETE FROM users WHERE id = :id", {'id': 8})

#데이터 삭제3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

#중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

#테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

#커밋
conn.commit()

#접속 해제
conn.close()
