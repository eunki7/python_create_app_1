import pymysql
import simplejson as json

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                       db='python_app1', charset='utf8') #autocommit=True

try:
    with conn.cursor() as c: #딕셔너리 반환 : conn.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM users")
        #1개 로우 선택
        print(c.fetchone())
        #지정 로우 선택
        print(c.fetchmany(3))
        #전체 로우 선택
        print(c.fetchall())

        #순회1
        c.execute("SELECT * FROM users ORDER BY id ASC")
        rows = c.fetchall()
        for row in rows:
            print('usage1 >',row)

        #순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('usage2 >',row)

        #조건 조회1
        param1 = (1,)
        c.execute('SELECT * FROM users WHERE id=%s', param1)
        #print('param1',c.fetchone())
        print('param1',c.fetchall())

        #조건 조회2
        param2 = 1
        c.execute("SELECT * FROM users WHERE id='%s'" % param2)
        #print('param2',c.fetchone())
        print('param2',c.fetchall())

        #조건 조회3
        param4 = (1,4)
        c.execute('SELECT * FROM users WHERE id IN(%s,%s)', param4)
        print('param3',c.fetchall())

        #조건 조회4
        c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4)) # python formatting %s, %d, %f...
        print('param4',c.fetchall())

        #조건 조회5
        c.execute("SELECT * FROM users WHERE id In(%s,%s)" % (1, 4))
        print('param5',c.fetchall())

    #conn.commit()
finally:
    conn.close()
