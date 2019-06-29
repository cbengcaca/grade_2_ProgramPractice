import pymysql

class DBOpr_ReaderConnection:
    def insert(self, insertList):
        self.selSQL = ''
        self.selSQL = 'INSERT INTO t_readerconnection VALUES('
        self.selSQL += str(insertList[0])
        self.selSQL += ','
        self.selSQL += str(insertList[1])
        self.selSQL += ');'
        return self.selSQL

    def delete(self, readerId):
        self.selSQL = ''
        self.selSQL = 'DELETE FROM t_readerconnection WHERE readerId = '
        self.selSQL += str(readerId)
        self.selSQL += ';'
        return self.selSQL

a = DBOpr_ReaderConnection()
x = 22
List=[x,13842191924]
a.insert(List)
#a.delete(20)