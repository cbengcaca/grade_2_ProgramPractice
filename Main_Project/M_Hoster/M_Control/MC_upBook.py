from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
from M_Hoster.Action_constructor.Acon_upBook import Acon_UpBook

class MC_UpBook:
    def __init__(self):
        self.creater = Acon_UpBook()
        self.runner = M_SqlRunner()

    def searchIfIsbnExist(self,infoList):
        isbn = infoList[1]
        sql = self.creater.searchIfIsbnExist(isbn)
        sqlList = [sql]
        ret = self.runner.beginSql(sqlList)
        return ret

    def getNextBookId(self):
        sql = self.creater.getNextBookId()
        sqlList = [sql]
        ret = self.runner.beginSql(sqlList)
        return ret

    def getShelfMessage(self):
        sql = self.creater.getAvailableShelf()
        sqlList = [sql]
        ret = self.runner.beginSql(sqlList)
        return ret

    def addNewBook_exist(self,infoList):
        sqlList = []
        isbn = infoList[1]
        operId = infoList[2]
        shelfId = infoList[3]
        bookId = self.getNextBookId()
        sqlList.append(self.creater.changeBookStock(isbn))
        sqlList.append(self.creater.upBook(operId, isbn, shelfId, bookId))
        status = self.runner.beginSql(sqlList)
        if status is not 'ERROR':
            return '1'

    def addNewBook_notexist(self,infoList):
        isbn = infoList[1]
        bookName = infoList[2]
        bookAuthor = infoList[3]
        bookPublisher = infoList[4]
        bookPrice = infoList[5]
        bookCreateTime = infoList[6]
        operId = infoList[7]
        shelfId = infoList[8]
        bookId = self.getNextBookId()
        sqlList = []
        sqlList.append(self.creater.addNewIsbn(isbn,bookName,bookAuthor,bookPublisher,bookPrice,bookCreateTime,bookMaxNum,bookAvailableNum,bookSaleNumber))
        sqlList.append(self.creater.upBook(operId,isbn,shelfId,bookId))
        status = self.runner.beginSql(sqlList)
        if status is not 'ERROR':
            return '1'