import time
class Lcon_BorrowList:
    def insert(self, bookID, UserID):
        sql = "Insert into t_borrowlist (bookId,readerId,borrowTime) value ('" \
              + bookID + "','" + UserID + "','" + str(time.strftime('%Y-%m-%d %H:%M:%S')) + "')"
        return sql

    def delete(self, borrowId):

        self.selSQL = 'DELETE FROM t_borrowlist WHERE borrowId = '
        self.selSQL += str(borrowId)
        self.selSQL += ';'
        return self.selSQL


