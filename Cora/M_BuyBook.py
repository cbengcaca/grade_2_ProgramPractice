import datetime
import pymysql

class M_BuyBook:
    def __init__(self, bookId):
        self.__bookId = bookId
        self.__isbn = self.getISBN()[0]
        self.__bookPrice = self.getPrice()[0]

    #连接数据库
    def connectDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    #获取书籍ISBN
    def getISBN(self):
        selSQL = 'SELECT ISBN'
        selSQL += ' FROM t_bookinfo'
        selSQL += ' WHERE bookId = %d'%(self.__bookId)
        ret = ''
        con = self.connectDB()
        cursor = con.cursor()
        try:
            cursor.execute(selSQL)
            ret = cursor.fetchone()  # 获取单个元组
            con.close()
        except Exception as e:
            print("error:unable to fetch data", e)
        return ret

    #获取价格
    def getPrice(self):
        #动态SQL查询语句
        selSQL = 'SELECT bookPrice'
        selSQL += ' FROM t_isbninfo'
        selSQL += ' WHERE ISBN = %s'%(self.__isbn)
        ret = ''
        con = self.connectDB()
        cursor = con.cursor()
        try:
            cursor.execute(selSQL)
            ret = cursor.fetchone()  #获取单个元组
            con.close()
        except Exception as e:
            print("error:unable to fetch data", e)
        return ret

    #若付款成功，更新书库中书籍数量信息
    def updateAmount(self):
        #动态更新语句
        upSQL = 'UPDATE t_isbninfo '
        upSQL += 'SET bookMaxNum = bookMaxNum - 1, bookAvailableNum = bookAvailableNum - 1, bookSaleNumber = bookSaleNumber + 1'
        upSQL += ' WHERE ISBN = %d'%(self.__isbn)
        ret = False
        con = self.connectDB()
        cursor = con.cursor()
        try:
            ret = cursor.execute(upSQL)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failure", e)
        con.close()
        return ret

    def delBookId(self):
        delSQL = 'DELETE FROM t_bookinfo WHERE bookId = %d'%(self.__bookId)
        ret = False
        con = self.connectDB()
        cursor = con.cursor()
        try:
            ret = cursor.execute(delSQL)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failure", e)
        con.close()
        return ret

    #若付款成功，则增加一个已完成订单
    def addDeal(self):
        #动态insert语句
        inSQL = "INSERT INTO t_deal (dealTime, dealPrice, ISBN) VALUES('"
        inSQL += datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "','"
        inSQL += "%s"%(self.__bookPrice) + "','" + "%d"%(self.__isbn) + "')"
        ret = ''
        con = self.connectDB()
        cursor = con.cursor()
        try:
            ret = cursor.execute(inSQL)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failure", e)
        con.close()
        return ret

if __name__=='__main__':
    p = M_BuyBook(27)
    if p.updateAmount():
        print("success")
    if p.delBookId():
        print ("success")
    if p.addDeal():
        print("success")