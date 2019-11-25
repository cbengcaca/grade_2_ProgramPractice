
class Acon_AdminLogin:
    def setSql(self,userId,userPwd):
        sql = "SELECT operid,operPwd from t_oper where "
        sql += "operId = " + userId + " and operPwd = " + userPwd
        return sql