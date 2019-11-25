import datetime
import pymysql
from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner

class MC_BuyBook:
    def __init__(self, bookId, payFlag):
        self.__bookId = int(bookId)
        self.__payFlag = int(payFlag)
        # self.__isbn = self.getISBN()[0][0]
        # self.__bookPrice = self.getPrice()[0][0]
        self.__sqlList = []

    #获取书籍ISBN
    def getISBN(self):
        sqlRunner1 = M_SqlRunner()
        selISBNSQL = ['SELECT ISBN FROM t_bookinfo WHERE bookId = %d'%(self.__bookId)]
        ret = sqlRunner1.beginSql(selISBNSQL)
        return ret

    #获取价格
    def getPrice(self):
        #动态SQL查询语句
        isbn = self.getISBN()[0][0]
        sqlRunner2 = M_SqlRunner()
        selPriceSQL = ['SELECT bookPrice FROM t_isbninfo WHERE ISBN = %s'%(isbn)]
        ret = sqlRunner2.beginSql(selPriceSQL)
        return ret

    #若付款成功，生成更新书库中书籍数量信息的动态SQL语句
    def updateAmount(self):
        #动态更新语句
        upSQL = 'UPDATE t_isbninfo '
        upSQL += 'SET bookMaxNum = bookMaxNum - 1, bookAvailableNum = bookAvailableNum - 1, bookSaleNumber = bookSaleNumber + 1'
        upSQL += ' WHERE ISBN = %d'%(self.getISBN()[0][0])
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
        inSQL += "%s"%(self.getPrice()[0][0]) + "','" + "%d"%(self.getISBN()[0][0]) + "')"
        return inSQL

    def buybook(self):

        sqlRunner = M_SqlRunner()
        # 从界面中获取的书籍id不存在，则返回0

        if self.getISBN() == ():
            return '2'
        else:
        #若已支付成功，则进行数据库操作，返回数据库操作结果
            if self.__payFlag == 1:
                self.__sqlList.append(self.updateAmount())
                self.__sqlList.append(self.addDeal())
                self.__sqlList.append(self.delBookId())
                ret = sqlRunner.beginSql(self.__sqlList)
                return ret
            else:
                return '3'

if __name__=='__main__':
    p = MC_BuyBook('27', '0')
    ret = p.buybook()
    print(ret)