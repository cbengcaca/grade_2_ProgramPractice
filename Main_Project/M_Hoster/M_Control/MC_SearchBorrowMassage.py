from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
from M_Hoster.Action_constructor.Acon_SearchBorrowMassage import Acon_SearchBorrowMassage

class MC_SearchBorrowMassage:

    def __init__(self):
        self.creater = Acon_SearchBorrowMassage()
        self.runner = M_SqlRunner()

    def getSearchBorrow(self):
        sql = self.creater.setSearch()
        sqlList = [sql]
        borrowList = self.runner.beginSql(sqlList)
        return borrowList



