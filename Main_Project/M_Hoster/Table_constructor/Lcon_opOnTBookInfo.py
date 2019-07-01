
class Lcon_opOnBookInfo():
    def add(self, bookid,bookIsbn):
        self.sql = ''
        self.sql += "insert into t_bookinfo set bookid = " + bookid
        self.sql += ",bookIsbn = " + bookIsbn
        self.sql += ";"

        return self.sql
    #自带批量删除组件
    def delete(self, bookid,isbn):
        self.sql = ''
        flag = 0
        self.sql += "delete from t_bookinfo "
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

        return self.sql
