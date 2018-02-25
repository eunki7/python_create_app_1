import sqlite3

#DB생성(파일)
conn = sqlite3.connect('C:/Django/workspace/python-class1/section5/database/sqlite.db')

#커서 바인딩
c = conn.cursor()

#데이터 조회(전체)
c.execute("SELECT * FROM users")

#1개 로우 선택
print(c.fetchone())

#지정 로우 선택
print(c.fetchmany(size=3))

#전체 로우 선택
print(c.fetchall())

#순회1
rows = c.fetchall()
for row in rows:
    print('usage1 >',row)

#순회2
for row in c.fetchall():
    print('usage2 >',row)

#순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('usage3 > ',row)

#조건 조회1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1',c.fetchone())
print('param1',c.fetchall())

#조건 조회2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2) #%s %d
print('param2',c.fetchone())
print('param2',c.fetchall())

#조건 조회3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3',c.fetchone())
print('param3',c.fetchall())

#조건 조회4
param4 = (1,4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4',c.fetchall())

#조건 조회5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5',c.fetchall())

#조건 조회6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6',c.fetchall())


with conn:
    #Dump 출력
    with open('C:/Django/workspace/python-class1/section5/database/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')
