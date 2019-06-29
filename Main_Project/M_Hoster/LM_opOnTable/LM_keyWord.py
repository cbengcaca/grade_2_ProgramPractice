import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_keyWord(LM_superDBOp):
    def __init__(self):
        super(LM_keyWord, self).__init__()

    def add(self,keyWordContext):
        self.sql += "insert into t_keyword set keyWordContext = "
        self.sql += "'" + keyWordContext + "'"

    def delete(self,keyWordId):
        self.sql += "delete from t_keyword where "
        self.sql += "keyWordId = '" + keyWordId + "'"
