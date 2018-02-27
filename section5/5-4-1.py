import pymysql
import simplejson as json
import datetime

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                       db='python_app1', charset='utf8') #autocommit=True

#pyMysql 버전확인
print('pymysql.version : ',pymysql.__version__)

#데이터베이스 선택
conn.select_db('DB명')

#Cursor연결
c = conn.cursor()
print(type(c))

#데이터베이스 생성
c.execute('create database pytnon_app2') #DDL, DML, DCL 사용 가능

#커서 반환
c.close()

#접속 해제
conn.close()

#트랜잭션 시작
conn.begin()

#커밋
conn.commit()

#롤백
conn.rollback()

#날짜 생성
now = datetime.datetime.now()
print('now',now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)


#테이블 생성(데이터 타입 : 공식 레퍼런스 참조 또는 검색 참조)
c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                                            username varchar(20) NOT NULL, \
                                            email varchar(30),  \
                                            phone varchar(30), \
                                            website varchar(30), \
                                            regdate varchar(20) NOT NULL, PRIMARY KEY(id))" \
                                            ) #default, AUTO_INCREMENT

try:
    with conn.cursor() as c:
        #데이터 삽입(개별)
        c.execute("INSERT INTO users VALUES (1 ,'kim','kim@naver.com', '010-0000-0000', 'kim.com', %s)", (nowDatetime,))
        c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", (2, 'park', 'park@naver.com', '010-1111-1111', 'park.com', nowDatetime))

        #데이터 삽입(Many)(튜플, 리스트 가능)
        userList = (
            (3 ,'lee','lee@naver.com', '010-2222-2222', 'lee.com', nowDatetime),
            (4 ,'cho','cho@naver.com', '010-3333-3333', 'cho.com', nowDatetime),
            (5 ,'noh','noh@naver.com', '010-4444-4444', 'noh.com', nowDatetime)
        )
        c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", userList)

    conn.commit()
finally:
    conn.close()


try:
    with conn.cursor() as c:
        #JSON to MySQL 삽입1
        with open('C:/Django/workspace/python-class1/section5/data/users.json','r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
                userData.append(t)
            c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", userData)
            #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", tuple(userData))
    conn.commit()
finally:
    conn.close()


try:
    with conn.cursor() as c:
        #JSON to MySQL 삽입2
        with open('C:/Django/workspace/python-class1/section5/data/users.json','r') as infile:
            r = json.load(infile)
            for user in r:
                c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime))
        #테이블 Row 삭제
        print("users db deleted : ", c.execute("delete from users"), "rows")
    conn.commit()
finally:
    conn.close()
