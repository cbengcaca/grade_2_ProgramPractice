import pymysql

class DBOpr_ReaderBasicInfo:

    def connectReaderBasicInfoDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    def insert(self, insertList):

        self.selSQL = 'INSERT INTO t_readerbasicinfo VALUES(%s,%s,%s,%s);'
        self.selSQL += str(insertList[0])
        self.selSQL += ','
        self.selSQL += str(insertList[1])
        self.selSQL += ','
        self.selSQL += str(insertList[2])
        self.selSQL += ','
        self.selSQL += str(insertList[3])
        self.selSQL += ');'
        self.dbOpr()

    def delete(self, readerId):

        self.selSQL = 'DELETE FROM t_readerbasicinfo WHERE readerId = '
        self.selSQL += str(readerId)
        self.selSQL += ';'
        self.dbOpr()

    def dbOpr(self):

        db = self.connectReaderBasicInfoDB()
        cur = db.cursor()
        result = cur.execute(self.selSQL)
        db.commit()
        cur.close()
        db.close()



a = DBOpr_ReaderBasicInfo()
List=[1,1,'男',20]
a.insert(List)
#a.delete(20)