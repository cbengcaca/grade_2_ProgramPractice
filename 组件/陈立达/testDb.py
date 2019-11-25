import pymysql
db = pymysql.connect("10.240.224.173","cGroupOne","123456","mysql" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()