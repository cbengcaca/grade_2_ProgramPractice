import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_opOnBookInfo(LM_superDBOp):
    def __init__(self):
        super(LM_opOnBookInfo, self).__init__()

    def add(self, bookIsbn):
        self.sql += "insert into T_BookInfo set isbn = "
        self.sql += bookIsbn
        self.sql += ";"

    #自带批量删除组件
    def delete(self, bookid,isbn):
        flag = 0
        self.sql += "delete from T_BookInfo "
        if bookid is not "None":
            flag += 1
            if flag is 1:
                self.sql += "where "
            self.sql += "bookid = '" + bookid + "'"

        if isbn is not "None":
            flag += 1
            if flag is 1:
                self.sql += "where "
            else:
                self.sql += "AND"
            self.sql += "isbn = '" + isbn + "'"

a = LM_opOnBookInfo()

a.delete('None','1')
#a.update('1','5')
a.beginSql()
