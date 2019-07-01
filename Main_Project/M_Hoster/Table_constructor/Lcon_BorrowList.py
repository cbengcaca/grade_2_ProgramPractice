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



#a = DBOpr_BorrowList()
#x = 20
#List=[x,1,20,'2019-06-29 21:15:59.0000']
#a.insert(List)
#a.delete(20)