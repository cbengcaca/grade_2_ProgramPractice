import pymysql

class DBOpr_ReaderConnection:

    def connectReaderConnectionDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    def insert(self, insertList):

        self.selSQL = 'INSERT INTO t_readerconnection VALUES('
        self.selSQL += str(insertList[0])
        self.selSQL += ','
        self.selSQL += str(insertList[1])
        self.selSQL += ');'
        self.dbOpr()

    def delete(self, readerId):

        self.selSQL = 'DELETE FROM t_readerconnection WHERE readerId = '
        self.selSQL += str(readerId)
        self.selSQL += ';'
        self.dbOpr()

    def dbOpr(self):

        db = self.connectReaderConnectionDB()
        cur = db.cursor()
        result = cur.execute(self.selSQL)
        db.commit()
        cur.close()
        db.close()



a = DBOpr_ReaderConnection()
x = 22
List=[x,13842191924]
a.insert(List)
#a.delete(20)