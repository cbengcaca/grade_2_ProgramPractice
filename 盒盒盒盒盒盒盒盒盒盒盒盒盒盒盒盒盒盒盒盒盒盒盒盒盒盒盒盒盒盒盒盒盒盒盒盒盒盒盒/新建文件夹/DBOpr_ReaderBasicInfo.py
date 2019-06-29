import pymysql

class DBOpr_ReaderBasicInfo:

    def connectReaderBasicInfoDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    def insert(self, insertList):

        self.selSQL = 'INSERT INTO t_readerbasicinfo VALUES(%s,%s,%s,%s);'
        self.readerId = insertList[0]  # 接单号
        self.readerName = insertList[1]  # 书号
        self.readerSex = insertList[2]  # 读者id
        self.readerCreditScore = insertList[3]  # 借书时间
        self.args = (self.readerId, self.readerName, self.readerSex, self.readerCreditScore)
        self.dbOpr()

    def delete(self, readerId):

        self.selSQL = 'DELETE FROM t_readerbasicinfo WHERE readerId = %s;'
        self.readerId = readerId
        self.args = (self.readerId)
        self.dbOpr()

    def dbOpr(self):

        db = self.connectReaderBasicInfoDB()
        cur = db.cursor()
        result = cur.execute(self.selSQL, self.args)
        db.commit()
        cur.close()
        db.close()



a = DBOpr_ReaderBasicInfo()
List=[1,1,'男',20]
a.insert(List)
#a.delete(20)