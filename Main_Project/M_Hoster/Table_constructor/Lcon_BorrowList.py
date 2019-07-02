class Lcon_BorrowList:
    def insert(self, insertList):
        self.selSQL = 'INSERT INTO t_borrowlist VALUES('
        self.selSQL += str(insertList[0])
        self.selSQL += ','
        self.selSQL += str(insertList[1])
        self.selSQL += ','
        self.selSQL += str(insertList[2])
        self.selSQL += ','
        self.selSQL += str(insertList[3])
        self.selSQL += ');'
        return self.selSQL

    def delete(self, borrowId):

        self.selSQL = 'DELETE FROM t_borrowlist WHERE borrowId = '
        self.selSQL += str(borrowId)
        self.selSQL += ';'
        return self.selSQL


