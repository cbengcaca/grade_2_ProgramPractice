from M_Hoster.Action_constructor.Acon_devideWordsOp import Acon_devideWordsOp
from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
class MC_devideWords:
    def devideWords(self,searchList):
        sqlCreate = Acon_devideWordsOp()
        sql = sqlCreate.setSearch(searchList)
        sqlList = [sql]
        sqlRunner = M_SqlRunner()
        ret = sqlRunner.beginSql(sqlList)
        return ret