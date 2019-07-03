from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner


class MC_SearchNormal:
    def __init__(self):
        self.runner = M_SqlRunner()

    def getSearchNormal(self, sql):
        sqlList = [sql[0]]
        ret = self.runner.beginSql(sqlList)
        if(ret == '-1'):
            return [[0]]
        else :
            return ret

