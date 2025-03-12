import pymysql 
conn = pymysql.connect(host='127.0.0.1', user= 'root', password='0000', db='soloDB', charset='utf8')
cur = conn.cursor()
cur.execute("""
	CREATE TABLE userTable (
		ID CHAR(4),
		userName CHAR(15),
		email CHAR(20),
		birthYear INT
	)
""")
conn.commit()
cur.execute("insert into userTTTable values('hong', '홍지윤', 'hong@naver.com', 1996)")
cur.execute("insert into userTTTable values('kim ', '김태연', 'kim@daum.net', 2011)")
cur.execute("insert into userTTTable values('star', '별사랑', 'star@paran.com', 1990)")
cur.execute("insert into userTTTable values('yang', '양지은', 'yang@gmail.com', 1993)")


import pymysql
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
cur = conn.cursor()
cur.execute("select * from userTTTable")
print("사용자 ID    사용자 이름    이메일    출생연도")
print("------------------------------------------------")
while (True) :
    row = cur.fetchone()
    if row == None :
        break   
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s %15s %20s %5d" % (data1, data2, data3, data4))

conn.close()