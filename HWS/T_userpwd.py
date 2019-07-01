class T_userid:
    def add(self,readerID,pwd):
        sql="insert into t_userpwd(readerId,readerPwd) values('"+readerID+"','"+pwd+"');"
        return sql
    def dele(self,readerID):
        sql = "delete from t_userpwd where readerId='" + readerID + "'"
        return sql