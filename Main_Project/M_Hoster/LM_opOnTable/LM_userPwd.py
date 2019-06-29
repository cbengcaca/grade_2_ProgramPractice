import pymysql

class T_userid:

    def add(self,readerID,pwd):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql="insert into t_userpwd(readerId,readerPwd) values('"+readerID+"','"+pwd+"');"
        return sql

    def delete(self,readerID):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "delete from t_userpwd where readerId='" + readerID + "'"
        return sql
#db = T_userid("106.52.87.149", "root", "000000", "softwarePractice")
#db.add("20190300","0300")