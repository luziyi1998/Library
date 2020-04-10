import pymysql

conn = pymysql.connect(
    host="cdb-mg4o2vhq.cd.tencentcdb.com",
    port=10089,
    user="root", password="llx17121541",
    database="Library",
    charset="utf8")

cursor = conn.cursor()
conn.close()
print("asd")