from M_SqlRunner import *
class M_SignIn:
    def sign(UserID,pwd):
        sql = "SELECT readerPwd from t_userpwd where readerId = '"+UserID+"'"
        list = []
        list.append(sql)
        run = M_SqlRunner()
        result = run.beginSql(list)
        if result and result[0][0] == pwd:
            return 1
        else:
            return 0