import datetime
import pymysql
from M_SqlRunner import M_SqlRunner

class M_BuyBook:
    def __init__(self, bookId):
        self.__bookId = bookId
        self.__sqlRunner = M_SqlRunner()
        self.__isbn = self.getISBN()[0][0]
        self.__bookPrice = self.getPrice()[0][0]
        self.__sqlList = []

    #获取书籍ISBN
    def getISBN(self):
        selISBNSQL = ['SELECT ISBN FROM t_bookinfo WHERE bookId = %d'%(self.__bookId)]
        ret = self.__sqlRunner.beginSql(selISBNSQL)
        return ret

    #获取价格
    def getPrice(self):
        #动态SQL查询语句
        selPriceSQL = ['SELECT bookPrice FROM t_isbninfo WHERE ISBN = %s'%(self.__isbn)]
        ret = self.__sqlRunner.beginSql(selPriceSQL)
        return ret

    #若付款成功，生成更新书库中书籍数量信息的动态SQL语句
    def updateAmount(self):
        #动态更新语句
        upSQL = 'UPDATE t_isbninfo '
        upSQL += 'SET bookMaxNum = bookMaxNum - 1, bookAvailableNum = bookAvailableNum - 1, bookSaleNumber = bookSaleNumber + 1'
        upSQL += ' WHERE ISBN = %d'%(self.__isbn)
        return upSQL

    #若付款成功，生成删除书籍Id的动态语句
    def delBookId(self):
        delSQL = 'DELETE FROM t_bookinfo WHERE bookId = %d'%(self.__bookId)
        return delSQL

    #若付款成功，生成增加一个已完成订单的insert动态SQL语句
    def addDeal(self):
        #动态insert语句
        inSQL = "INSERT INTO t_deal (dealTime, dealPrice, ISBN) VALUES('"
        inSQL += datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "','"
        inSQL += "%s"%(self.__bookPrice) + "','" + "%d"%(self.__isbn) + "')"
        return inSQL

    def buybook(self):
        self.__sqlList.append(self.updateAmount())
        self.__sqlList.append(self.addDeal())
        self.__sqlList.append(self.delBookId())
        self.__sqlRunner.beginSql(self.__sqlList)

if __name__=='__main__':
    p = M_BuyBook(27)
    p.buybook()