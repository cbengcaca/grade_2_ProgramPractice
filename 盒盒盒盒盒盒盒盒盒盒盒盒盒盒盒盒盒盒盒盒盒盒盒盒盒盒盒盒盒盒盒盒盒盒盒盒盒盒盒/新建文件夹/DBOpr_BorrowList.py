import pymysql

class DBOpr_BorrowList:

    def connectBorrowListDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    def insert(self, insertList):

        self.selSQL = 'INSERT INTO t_borrowlist VALUES(%s,%s,%s,%s,NULL);'
        self.borrowId = insertList[0]  # 接单号
        self.bookId = insertList[1]  # 书号
        self.readerId = insertList[2]  # 读者id
        self.borrowTime = insertList[3]  # 借书时间
        self.args = (self.borrowId, self.bookId, self.readerId, self.borrowTime)
        self.dbOpr()

    def delete(self, borrowId):

        self.selSQL = 'DELETE FROM t_borrowlist WHERE borrowId = %s;'
        self.borrowId = borrowId
        self.args = (self.borrowId)
        self.dbOpr()

    def dbOpr(self):

        db = self.connectBorrowListDB()
        cur = db.cursor()
        result = cur.execute(self.selSQL, self.args)
        db.commit()
        cur.close()
        db.close()



a = DBOpr_BorrowList()
x = 20
List=[x,1,20,'2019-06-29 21:15:59.0000']
a.insert(List)
#a.delete(20)