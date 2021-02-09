# sec 12-2
# 파이썬 데이터베이스 연동
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)

conn = sqlite3.connect("./database.db")  # 내 db 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 한개 row 선택
# print(c.fetchone())

# 지정로우 선택
# print(c.fetchmany(size=3))


# 전체 로우 선택
# print(c.fetchall())

# 커서가 이동하면서 다음데이터의 위치를 기억하고 있다.


# 순회 1
# rows = c.fetchall()

# for data in rows:
#    print("show:", data)

# 순회 2
for row in c.fetchall():
    print(row)

# 순회 3
# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#    print(row)


print()

# WHERE Retrieve1

param1 = (3,)
c.execute("SELECT * FROM users WHERE id=?", param1)

print(c.fetchone())
print(c.fetchall())  # 데이터 없음

# WHERE Retrieve2

param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %f, %s, %d

print(c.fetchone())
print(c.fetchall())  # 데이터 없음

# WHERE Retrieve3

param3 = 4
c.execute("SELECT * FROM users WHERE id=:id", {"id": 4})
print(c.fetchone())
print(c.fetchall())  # 데이터 없음


# WHERE Retrieve 4
param4 = (1, 3)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print(c.fetchall())

# WHERE Retrieve 5
c.execute("SELECT * FROM users WHERE id IN(%d,%d)" % (3, 4))
print(c.fetchall())

# WHERE Retrieve 6
c.execute("SELECT * FROM users WHERE id =:id1 OR id=:id2",
          {"id1": 1, "id2": 3})
print(c.fetchall())


# Dump 출력 #서버가 바뀌면 덤프 떠와 한다
# db 분할설계 해야함...ㅋㅋㅋㅋ

with conn:
    with open("./dump.sql", "w") as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("dump print complite")
