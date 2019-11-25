from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
from M_Hoster.Action_constructor.Acon_searchReader import Acon_SearchReader
class MC_SearchReader:
    def searchReader(self):
        creater = Acon_SearchReader()
        runner = M_SqlRunner()
        sql = creater.setSearch()
        sqlList = [sql]
        ret = runner.beginSql(sqlList)
        return ret
