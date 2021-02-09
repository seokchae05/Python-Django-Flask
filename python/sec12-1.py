# sec 12-1
# 파이썬 데이터베이스 연동 sqlLite
# 테이블 생성 및 삽입


import sqlite3
import datetime

# 삽입할 날짜 생성

now = datetime.datetime.now()
print(now)

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowDateTime)


print(sqlite3.version)
print(sqlite3.sqlite_version)


# db 생성 및 auto commit(Rollback)

conn = sqlite3.connect(
    'C:/Users/user/Desktop/fastcampus/python/database.db', isolation_level=None)

# Curser

c = conn.cursor()

print(type(c))

# 테이블 생성(dataType : TEXT, NUMERIC, INTEGER, REAL,BLOB)

c.execute("CREATE TABLE IF NOT EXISTS users(id  INTEGER PRIMARY KEY, username text, email text, \
    phone text, website text, regdate text)")

# 데이터 삽입

c.execute("INSERT INTO users VALUES(1 ,'kim' ,'seokchae@naver.com' , '010-xxxx-1112','lee.com', ?)", (nowDateTime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",
          (2, 'lee', 'aaa@naver.com', '010-xxxx-5666', 'q.com', nowDateTime))


# Many 삽입(튜플, 리스트)
userlist = (
    (3, "king", "asda@naver.com", "010-2222-2222", "qa.com", nowDateTime),
    (4, "g", "add@naver.com", "010-3333-2132", "1.com", nowDateTime),
)

c.executemany(
    "INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userlist)


# 테이블 데이터 삭제

#print("user db deleted :", conn.execute("DELETE FROM users").rowcount)

# 커밋은 오토커밋 isolation_level: None
# conn.commit()


# 접속해제
conn.close()
