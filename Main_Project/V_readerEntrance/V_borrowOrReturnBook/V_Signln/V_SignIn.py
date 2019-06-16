from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import datetime

class V_SignIn:
    def __init__(self,main_Win):
        self.main_Win = main_Win
        self.__root=Tk()
        self.__root.title('登录')
        self.__root.geometry('420x120')
        self.__root.attributes("-toolwindow", 1)
        self.__root.wm_attributes("-topmost", 1)

        frm = Frame(self.__root)                    # 主界面起始
        frm_F = Frame(frm)                                  # 第一层起始

        frm_FL = Frame(frm_F)                                       # 第一层左起始
        Label(frm_FL, text='账号', font=('Arial', 12)).pack(side=TOP)
        Label(frm_FL, text='密码', font=('Arial', 12)).pack(side=TOP)
        frm_FL.pack(side=LEFT)                                      # 第一层左放置

        frm_FR = Frame(frm_F)                                       # 第一层右起始
        var_count = StringVar()
        self.__entryCount = Entry(frm_FR, textvariable=var_count, width=30, font=('Verdana', 15))
        self.__entryCount.pack()
        var_pwd = StringVar()
        self.__entryPwd = Entry(frm_FR, textvariable=var_pwd, width=30, font=('Verdana', 15))
        self.__entryPwd.pack()
        frm_FR.pack(side=RIGHT)                                     # 第一层右结束

        frm_F.pack(side=TOP)                                # 第一层结束

        frm_S = Frame(frm)                                  #第二层开始
        Button(frm_S, text="确认", command=self.ensure, width=6, height=1, font=('Arial', 10)).pack(side=LEFT)
        Button(frm_S, text="返回", command=self.__root.quit, width=6, height=1, font=('Arial', 10)).pack(side=RIGHT)
        frm_S.pack(side=BOTTOM)                             #第二层结束

        frm.pack()                                  # 主界面结束

        self.__root.mainloop()

    def ensure(self):
        #数据库校验账号信息
        count = self.__entryCount.get()
        pwd = self.__entryPwd.get()
        if count == '123' and pwd =='1234' :  # 操作成功
            a = tkinter.messagebox.showinfo('提示', '登录成功')
            self.main_Win.status=1
            self.__root.withdraw()
            self.__root.quit()
        else:  # 操作失败
            self.main_Win.status=0
            a = tkinter.messagebox.showerror('错误', '账号或密码错误！')
