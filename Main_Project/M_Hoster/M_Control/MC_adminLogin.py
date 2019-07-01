from M_Hoster.Action_constructor.Acon_adminLogin import Acon_AdminLogin
from M_Hoster.M_SqlRunner.M_SqlRunner import M_SqlRunner
class MC_AdminLogin:
    def beginCompare(self,logKey):
        userId = logKey[0]
        userPwd = logKey[1]
        creater = Acon_AdminLogin()
        runner = M_SqlRunner()
        sql = creater.setSql(userId,userPwd)
        sqlList = [sql]
        ret = runner.beginSql(sqlList)
        if ret:
            return '1'
        else:
            return '0'

