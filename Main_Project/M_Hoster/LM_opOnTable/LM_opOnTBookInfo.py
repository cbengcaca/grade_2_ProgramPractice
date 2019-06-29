from M_Hoster.M_Action.M_superDb import M_SuperDb
class LM_opOnBookInfo(M_SuperDb):
    def add(self, bookIsbn):
        self.sql = ''
        self.sql += "insert into t_bookinfo set isbn = "
        self.sql += bookIsbn
        self.sql += ";"
        self.beginSql(self.sql)
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

a = LM_opOnBookInfo()
a.add('5')