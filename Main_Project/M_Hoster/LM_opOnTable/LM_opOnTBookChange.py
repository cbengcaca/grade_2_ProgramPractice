
class LM_opOnTBookChange:
    def add(self,opType,operId,bookId):
        self.sql = ''
        self.sql += "insert into t_bookchange set "
        self.sql += "opType = "
        self.sql += "'" + opType + "'"
        self.sql += ",operId = "
        self.sql += operId
        self.sql += ",bookId = "
        self.sql += bookId
        self.sql += ",opTime = now()"

    def delete(self,opId):
        self.sql = ''
        self.sql += "delete from t_bookchange where opId = "
        self.sql += opId

#a = LM_opOnTBookChange()
#a.add('upbook','1','25')
#a.beginSql()