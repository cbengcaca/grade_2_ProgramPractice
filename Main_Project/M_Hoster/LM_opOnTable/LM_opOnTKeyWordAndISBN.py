import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_opOnTKeyWordAndISBN(LM_superDBOp):
    def __init__(self):
        super(LM_opOnTKeyWordAndISBN, self).__init__()

    def add(self,keyWordId,isbn):
        self.sql += "insert into t_keywordandisbn set "
        self.sql += "keyWordId = '" + keyWordId + "'"
        self.sql += ",isbn = '" + isbn + "'"

    def delete(self,keyWordId,isbn):
        flag = 0
        self.sql += "delete from t_keywordandisbn "
        if keyWordId is not "None":
            flag += 1
            if flag is 1:
                self.sql += "where"
            self.sql += "keyWordid = '" + keyWordId + "'"

        if isbn is not "None":
            flag += 1
            if flag is 1:
                self.sql += " where"
            else:
                self.sql += " AND"
            self.sql += "isbn = '" + isbn + "'"