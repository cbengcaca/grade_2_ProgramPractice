from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
class MC_UpBook:
    def fuction(self,isbn):
        a = getSqlClass()
        sql = a.getsql(isbn)

        sqlRunner = M_SqlRunner()
        ret = sqlRunner.beginSql(sql)

        if ret is '':
            b = getSqlClass()
            sql = b.getSqlIsbnAdd(isbn)
            sqlRunner.beginSql(sql)

            c = getSqlClass()


        else:
