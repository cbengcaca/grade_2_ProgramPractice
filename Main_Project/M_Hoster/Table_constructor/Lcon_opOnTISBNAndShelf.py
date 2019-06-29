
class Lcon_opOnTISBNAndShelf:
    def add(self,isbn,shelfid):
        self.sql = ''
        self.sql += "insert into t_isbnandshelf set "
        self.sql += "isbn = " + isbn
        self.sql += ",shelfid = " + shelfid

    def delete(self,isbn,shelfid):
        self.sql = ''
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