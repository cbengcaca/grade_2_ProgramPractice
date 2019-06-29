import pymysql
import tkinter.messagebox
class DBO:
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
    def CreateTabel(self,sql):
        db=self.ConnectDB()
        cursor=db.cursor()
        cursor.execute(sql)
        db.close()
    def Insert(self,sql):
        db=self.ConnectDB()
        cursor=db.cursor()
        #sql="insert into h_email(sender,receiver,title,context,p_date) values('"\
        #     +sender+"','"+receiver+"','"+title+"','"+time+"')'"
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print("Error:",e)
        db.close()
    def Delete(self,sql):
        db=self.ConnectDB()
        cursor=db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print("Error:",e)
        db.close()
    def Search(self,sql):
        ret=''
        db=self.ConnectDB()
        cursor=db.cursor()
        #sql="select id,sender,receiver,context,p_date,title from h_email where title like '"+title+"%'"
        try:
            cursor.execute(sql)
            ret=cursor.fetchall()
            db.commit()
        except Exception as e:
            db.rollback()
            print("Error:",e)
        db.close()
        return ret

#db=pymysql.connect("localhost","root",input("DB-PWD:"),"emaildb")
