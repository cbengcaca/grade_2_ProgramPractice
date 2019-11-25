import pymysql
from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
class Acon_SuperDb:
    def beginSql(self,sql):
        sqlRunner = M_SqlRunner()
        ret = sqlRunner.beginSql(sql)
        return ret