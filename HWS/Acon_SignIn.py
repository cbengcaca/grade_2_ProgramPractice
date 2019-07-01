def select_Pwd(UserID):
    sql = "SELECT readerPwd from t_userpwd where readerId = '" + UserID + "'"
    return sql