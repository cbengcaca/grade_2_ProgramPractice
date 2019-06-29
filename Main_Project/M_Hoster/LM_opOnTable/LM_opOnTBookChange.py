import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_opOnTBookChange(LM_superDBOp):
    def __init__(self):
        super(LM_opOnTBookChange, self).__init__()

    def add(self,opType,operId,bookId):
        self.sql += "insert into t_bookchange set "
        self.sql += "opType = "
        self.sql += "'" + opType + "'"
        self.sql += ",operId = "
        self.sql += operId
        self.sql += ",bookId = "
        self.sql += bookId
        self.sql += ",opTime = now()"

    def delete(self,opId):
        self.sql += "delete from t_bookchange where opId = "
        self.sql += opId

#a = LM_opOnTBookChange()
#a.add('upbook','1','25')
#a.beginSql()