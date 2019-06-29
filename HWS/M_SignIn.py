from dbtest import *
class M_SignIn:
    def sign(UserID,pwd):
        sql = "Select readerPwd from t_userpwd where readerId = '"+UserID+"'"
        db = DBO("106.52.87.149", "root", "000000", "softwarePractice")
        result = db.Search(sql)
        if result and result[0][0] == pwd:
            return 1
        else:
            return 0