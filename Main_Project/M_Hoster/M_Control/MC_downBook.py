from M_SqlRunner import M_SqlRunner
from Acon_downBook import Acon_downBook

class MC_downBook:
    def __init__(self):
        self.creater = Acon_downBook()
        self.runner = M_SqlRunner()

    def searchIfBookIdExist(self,infoList):
        bookId = infoList[1]
        sql1 = self.creater.searchIfBookIdExist(bookId)
        sqlList = [sql1]
        ret = self.runner.beginSql(sqlList)
        return ret


    def searchIsbn(self,infoList):
        bookId = infoList[1]
        sql2 = self.creater.searchIsbn(bookId)
        sqlList = [sql2]
        ret = self.runner.beginSql(sqlList)
        return ret

    def searchBorrowList(self,infoList):
        bookId = infoList[1]
        sql3 = self.creater.searchBorrowList(bookId)
        sqlList = [sql3]
        ret = self.runner.beginSql(sqlList)
        return ret


    def changeBookInfo(self,infoList):
        ret1 = self.searchIfBookIdExist(infoList)
        #如果Id存在
        if ret1:
            #查书籍id对应isbn
            isbn = self.searchIsbn(infoList)
            isbn =str(isbn[0][0])

            #查书籍是否借出
            ret2 = self.searchBorrowList(infoList)
            bookId = infoList[1]
            operId = infoList[2]
            sqlList = self.creater.changeInfo(bookId, isbn, operId, ret2)
            ret3 = self.runner.beginSql(sqlList)
            if ret3 is '0':
                return '1'
            else:
                return '0'
        else:
            return '0'







