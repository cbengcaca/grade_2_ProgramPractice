from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
from M_Hoster.Table_constructor.Lcon_opOnISBNInfo import Lcon_opOnISBNInfo
from M_Hoster.Table_constructor.Lcon_opOnTBookInfo import Lcon_opOnBookInfo
from M_Hoster.Table_constructor.Lcon_opOnTISBNAndShelf import Lcon_opOnTISBNAndShelf
from M_Hoster.Table_constructor.Lcon_opOnTBookChange import Lcon_opOnTBookChange
class Acon_UpBook:
    #获取isbn是否存在
    def searchIfIsbnExist(self,isbn):
        sql  = "SELECT isbn from t_isbninfo where isbn = " + isbn
        return sql

    #获取下一个bookid
    def getNextBookId(self):
        sqlGetNewBookId = "SELECT max(bookid) from t_bookinfo"
        return sqlGetNewBookId

    #isbn已存在
    def changeBookStock(self,isbn):
        sqlChange = "update t_isbninfo set bookMaxNum = bookMaxNum + 1 , bookAvailableNum = bookAvailableNum+1 where "
        sqlChange += "isbn = " + isbn
        return sqlChange

    #isbn新添加
    def addNewIsbn(self,isbn, shelfid,bookName, bookAuthor, bookPublisher, bookPrice, bookCreateTime,bookMaxNum='1', bookAvailableNum='1', bookSaleNumber='0'):
        isbninfoCreater = Lcon_opOnISBNInfo()

        sqlIsbninfo = isbninfoCreater.add(isbn, bookName, bookAuthor, bookPublisher, bookPrice, bookCreateTime,bookMaxNum, bookAvailableNum, bookSaleNumber)

        # isbn所在书架信息
        shelfCreater = Lcon_opOnTISBNAndShelf()
        sqlShelfinfo = shelfCreater.add(isbn, shelfid)

        sqlList = [sqlIsbninfo,sqlShelfinfo]
        return sqlList

    #获取可用书架信息
    def getAvailableShelf(self):
        sqlGetAvailableShelf = "SELECT * from t_shelfLocate"
        return sqlGetAvailableShelf

    def upBook(self,operId,isbn,bookid):
        #书本信息
        bookinfoCreater = Lcon_opOnBookInfo()
        sqlBookinfo = bookinfoCreater.add(bookid,isbn)


        #操作记录信息
        bookChange = Lcon_opOnTBookChange()
        sqlBookChange = bookChange.add("upBook",operId,bookid)

        sqlList = [sqlBookinfo,sqlBookChange]
        return sqlList












