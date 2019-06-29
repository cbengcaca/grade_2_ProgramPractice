import pymysql
class LM_superDBOp:
    def __init__(self):
        self.sql = ''

    def connectDB(self):
        db = pymysql.connect('localhost', 'root', '19990418sY', 'softwarepractice', autocommit=True)
        return db

    def beginSql(self):
        con = self.connectDB()
        cursor = con.cursor()
        try:
            cursor.execute(self.sql)
            con.close()
            print("operation done")
        except Exception as e:
            print("error:unable to fetch data", e)

