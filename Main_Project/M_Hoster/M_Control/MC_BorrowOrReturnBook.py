from M_Hoster.M_SqlRunner import M_SqlRunner
import time,datetime
from M_Hoster.Action_constructor import Acon_BorrowOrReturnBook
import pymysql
from M_Hoster.Table_constructor import Lcon_BorrowList
class MC_BorrowOrReturnBook:
    def Borrow(self,UserID,bookID):
        sql = "SELECT * from t_borrowlist where bookid = " + bookID
        list = [sql]
        runner = M_SqlRunner.M_SqlRunner()
        ret = runner.beginSql(list)
        if sql : #存在此书借阅记录
            sql = "SELECT * from t_borrowlist where bookid = " + bookID + " and returntime is Null"
            list = [sql]
            ret = runner.beginSql(list)
            if ret: #此书的借阅记录未归还
                return '-1'
            else:#此书已归还
                pass
        else:#不存在此书借阅记录
            pass

        list = []
        sql = Acon_BorrowOrReturnBook.select_isbn(bookID)
        list.append(sql)
        db = M_SqlRunner.M_SqlRunner()
        result = db.beginSql(list)
        if result:
            isbn = str(result[0][0])
            sql = Acon_BorrowOrReturnBook.update_num(isbn)
            list = []
            list.append(sql)                #isbn可用书籍数量建议
            # 借阅记录
            a = Lcon_BorrowList.Lcon_BorrowList()
            sql = a.insert(bookID, UserID)
            list.append(sql)
            return db.beginSql(list)
        else:
            return '-1'
    def Return(self,bookID):
        db = M_SqlRunner.M_SqlRunner()
        list=[]
        sql = Acon_BorrowOrReturnBook.select_borrowid(bookID)
        list.append(sql)
        result = db.beginSql(list)
        if result[0][0] == None:
            return '-1'
        sql = Acon_BorrowOrReturnBook.update_borrowlist(str(result[0][0]))
        list = []
        list.append(sql)
        return db.beginSql(list)
#a=M_BorrowOrReturnBook()
#a.Borrow("001","001")
#a.Return("001")
