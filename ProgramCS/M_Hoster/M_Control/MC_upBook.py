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
        if ret : ##书籍存在
            return '1'
        else:
            ##不存在返回书架信息
            sql = self.creater.getAvailableShelf()
            sqlList = [sql]
            ret = self.runner.beginSql(sqlList)
        return ret

    def getNextBookId(self):
        sql = self.creater.getNextBookId()
        sqlList = []
        sqlList.append(sql)
        ret = self.runner.beginSql(sqlList)[0][0]
        return ret

    def addNewBook_exist(self,infoList):
        sqlList = []
        isbn = infoList[0]
        operId = infoList[1]
        bookId = str(self.getNextBookId() +1)

        sqlList.append(self.creater.changeBookStock(isbn))
        sqlList += self.creater.upBook(operId, isbn, bookId)
        status = self.runner.beginSql(sqlList)
        if status is not '-1':
            return bookId
        else:
            return '0'

    def addNewBook_notexist(self,infoList):
        creater = Acon_UpBook()
        isbn = infoList[0]
        bookName = infoList[1]
        bookAuthor = infoList[2]
        bookPublisher = infoList[3]
        bookPrice = infoList[4]
        bookCreateTime = infoList[5]
        operId = infoList[6]
        shelfId = infoList[7]
        bookId = str(self.getNextBookId() +1 )
        sqlList = creater.addNewIsbn(isbn, shelfId, bookName, bookAuthor, bookPublisher, bookPrice, bookCreateTime)
        sqlList += self.creater.upBook(operId, isbn, bookId)
        status = self.runner.beginSql(sqlList)

        #添加成功 返回bookId
        if status is  not '-1':
            return bookId
        else:
            return '0'

