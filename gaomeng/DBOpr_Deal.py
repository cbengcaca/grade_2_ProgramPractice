import pymysql

class DBOpr_Deal:

    def connectDealDB(self):
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        return db

    def insert(self, insertList):
        self.sql = 'insert into t_deal values(%s,%s,%s,%s);'
        self.dealId = insertList[0]  #订单id
        self.dealTime = insertList[1]  # 交易时间
        self.dealPrice = insertList[2]  # 交易价格
        self.ISBN = insertList[3]  # 书编号
        self.args = (self.dealId, self.dealTime, self.dealPrice, self.ISBN)
        self.dbOpr()

    def delete(self, dealId):
        self.sql = 'DELETE FROM t_deal WHERE dealId = %s;'
        self.dealId = dealId
        self.args = (self.dealId)
        self.dbOpr()

    def dbOpr(self):
        db = self.connectDealDB()
        cur = db.cursor()
        result = cur.execute(self.sql, self.args)
        db.commit()
        cur.close()
        db.close()



a = DBOpr_Deal()
List = [1, '2019-06-29 11:10:59.0000', 20, 1]
a.insert(List)
# a.delete(1)
