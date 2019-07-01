from M_SqlRunner import *
import Acon_SignIn
class MC_SignIn:
    def sign(self,UserID,pwd):
        sql = Acon_SignIn.select_Pwd(UserID)
        list = []
        list.append(sql)
        run = M_SqlRunner()
        result = run.beginSql(list)
        if result and result[0][0] == pwd:
            return 1
        else:
            return 0