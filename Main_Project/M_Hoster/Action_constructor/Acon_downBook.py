from M_SqlRunner import M_SqlRunner
from Lcon_opOnBookInfo import Lcon_opOnBookInfo
from Lcon_opOnTBookChange import Lcon_opOnTBookChange

class Acon_downBook:
    #获取bookId是否存在
    def searchIfBookIdExist(self,bookId):
        sql  = "SELECT bookId from t_bookinfo where bookId = " + bookId
        return sql

    def searchIsbn(self,bookId):
        sql  = "SELECT ISBN from t_bookinfo where bookId = " + bookId
        return sql

    def searchBorrowList(self,bookId):
        sql  = "SELECT bookId from t_borrowlist where bookId = " + bookId
        return sql

    #书籍未借出情况，可借数量减一
    def changeBookStock1(self,isbn):
        sqlChange = "update t_isbninfo set bookMaxNum = bookMaxNum - 1 , bookAvailableNum = bookAvailableNum-1 where "
        sqlChange += "isbn = " + isbn
        return sqlChange

    #书籍借出情况，可借数量不变
    def changeBookStock2(self,isbn):
        sqlChange = "update t_isbninfo set bookMaxNum = bookMaxNum - 1 where "
        sqlChange += "isbn = " + isbn
        return sqlChange

    def changeInfo(self,bookId, isbn, operId, ret):
        opOnBookInfo =Lcon_opOnBookInfo()
        sqlBookInfo = opOnBookInfo.delete(bookId, 'None')

        if ret:
            sqlIsbnInfo = self.changeBookStock2(isbn)
        # 若书籍未借出
        else:
            sqlIsbnInfo = self.changeBookStock1(isbn)

        opOnBookChange = Lcon_opOnTBookChange()
        sqlBookChange = opOnBookChange.add("downBook",operId,bookId)

        sqlList = [sqlBookInfo, sqlIsbnInfo, sqlBookChange]
        return sqlList
