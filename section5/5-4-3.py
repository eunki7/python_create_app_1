import pymysql
import simplejson as json

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                       db='python_app1', charset='utf8') #autocommit=True

try:
    with conn.cursor() as c: #딕셔너리 반환 : conn.cursor(pymysql.cursors.DictCursor)
        #데이터 수정1
        c.execute("UPDATE users SET username = %s WHERE id = %s", ('niceman', 1))
        #데이터 수정2
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('cuteboy', 5))

        #중간데이터 확인1
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 >',row)

        #데이터 삭제1
        c.execute("DELETE FROM users WHERE id = %s", (7,))

        #데이터 삭제2
        c.execute("DELETE FROM users WHERE id = '%d'" % 9)

        #중간데이터 확인2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check2 >',row)

        #로우 카운트
        print('rowCount : ',c.execute("SELECT * FROM users ORDER BY id DESC"))

    conn.commit()
finally:
    conn.close()
