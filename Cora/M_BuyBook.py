import datetime
import pymysql

class M_BuyBook:
    def __init__(self, isbn):
        self.__isbn = isbn

    #连接数据库
    def connectDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    #获取价格
    def getPrice(self):
        #动态SQL查询语句
        selSQL = 'SELECT bookPrice'
        selSQL += ' FROM t_isbninfo'
        selSQL += ' WHERE ISBN = %d'%(self.__isbn)
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

    #若付款成功，则增加一个已完成订单
    def addDeal(self):
        #动态insert语句
        inSQL = "INSERT INTO t_deal (dealTime, dealPrice, ISBN) VALUES('"
        inSQL += datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "','"
        inSQL += "%s"%(self.getPrice()[0]) + "','" + "%d"%(self.__isbn) + "')"
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
    p = M_BuyBook(2)
    print(p.getPrice()[0])
    if p.updateAmount():
        print("success")
    if p.addDeal():
        print("success")