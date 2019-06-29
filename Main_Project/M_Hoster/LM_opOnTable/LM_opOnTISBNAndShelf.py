import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_opOnTISBNAndShelf(LM_superDBOp):
    def __init__(self):
        super(LM_opOnTISBNAndShelf, self).__init__()

    def add(self,isbn,shelfid):
        self.sql += "insert into t_isbnandshelf set "
        self.sql += "isbn = " + isbn
        self.sql += ",shelfid = " + shelfid

    def delete(self,isbn,shelfid):
        flag = 0
        self.sql += "delete from t_isbnandshelf "
        if isbn != "None":
            flag += 1
            if flag is 1:
                self.sql += "where "
            self.sql += "isbn = '" + isbn + "'"

        if shelfid != "None":
            flag += 1
            if flag is 1:
                self.sql += "where "
            else:
                self.sql += "AND "
            self.sql += "shelfid = '" + shelfid + "'"

a = LM_opOnTISBNAndShelf()
a.delete('1','0')
a.beginSql()