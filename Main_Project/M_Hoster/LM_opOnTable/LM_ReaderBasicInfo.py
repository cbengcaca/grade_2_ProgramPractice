class DBOpr_ReaderBasicInfo:

    def insert(self, insertList):
        self.selSQL = ''
        self.selSQL = 'INSERT INTO t_readerbasicinfo VALUES(%s,%s,%s,%s);'
        self.readerId = insertList[0]  # 接单号
        self.readerName = insertList[1]  # 书号
        self.readerSex = insertList[2]  # 读者id
        self.readerCreditScore = insertList[3]  # 借书时间
        self.args = (self.readerId, self.readerName, self.readerSex, self.readerCreditScore)
        return self.selSQL

    def delete(self, readerId):
        self.selSQL = ''
        self.selSQL = 'DELETE FROM t_readerbasicinfo WHERE readerId = %s;'
        self.readerId = readerId
        self.args = (self.readerId)
        return self.selSQL

a = DBOpr_ReaderBasicInfo()
List=[1,1,'男',20]
a.insert(List)
#a.delete(20)