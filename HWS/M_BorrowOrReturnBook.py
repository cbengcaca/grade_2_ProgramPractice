from M_SqlRunner import *
import time,datetime
import pymysql
class M_BorrowOrReturnBook:
    def Borrow(self,UserID,bookID):
        list = []
        sql = "SELECT ISBN from t_bookinfo where bookId = '"+bookID+"'"
        list.append(sql)
        db = M_SqlRunner()
        result = db.beginSql(list)
        isbn = str(result[0][0])
        sql = "Update t_isbninfo set bookAvailableNum = bookAvailableNum-1 where ISBN = '"+isbn+"'"
        list = []
        list.append(sql)                #isbn可用书籍数量建议
        # 借阅记录
        sql = "Insert into t_borrowlist (bookId,readerId,borrowTime) value ('"\
              +bookID+"','"+UserID+"','"+str(time.strftime('%Y-%m-%d %H:%M:%S'))+"')"
        list.append(sql)
        db.beginSql(list)
    def Return(self,bookID):
        db = M_SqlRunner()
        list=[]
        sql = "SELECT max(borrowId) from t_borrowlist where bookId = '" + bookID + "'"
        list.append(sql)
        result = db.beginSql(list)
        sql="Update t_borrowlist set returnTime = '"+str(time.strftime('%Y-%m-%d %H:%M:%S'))+"' where borrowId = '"\
            +str(result[0][0])+"'"
        list = []
        list.append(sql)
        db.beginSql(list)
a=M_BorrowOrReturnBook()
a.Borrow("001","001")
#a.Return("001")
