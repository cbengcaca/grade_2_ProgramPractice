import pymysql

class T_shelflocate:
    def __init__(self,IPAdress,DBuser,DBpwd,DBname):
        self.__IPAdress=IPAdress
        self.__DBuser=DBuser
        self.__DBpwd=DBpwd
        self.__DBname=DBname
    def __del__(self):
        print("DBO is closed")
    def ConnectDB(self):
        db=pymysql.connect(self.__IPAdress,self.__DBuser,self.__DBpwd,self.__DBname)
        return db
    def add(self,shelfID,locate):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql="insert into t_shelflocate(shelfId,shelflocate) values('"+shelfID+"','"+locate+"');"
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print("Error:", e)
        db.close()
    def dele(self,shelfID):
        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "delete from t_shelflocate where shelfId='" + shelfID + "'"
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print("Error:", e)
        db.close()

#db = T_shelflocate("106.52.87.149", "root", "000000", "softwarePractice")
#db.add("2019003","2")