import pymysql

class T_shelflocate:
    def add(self,shelfID,locate):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql="insert into t_shelflocate(shelfId,shelflocate) values('"+shelfID+"','"+locate+"');"
        return sql

    def delete(self,shelfID):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "delete from t_shelflocate where shelfId='" + shelfID + "'"
        return sql

#db = T_shelflocate("106.52.87.149", "root", "000000", "softwarePractice")
#db.add("2019003","2")