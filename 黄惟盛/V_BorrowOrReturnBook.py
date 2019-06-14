from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import datetime

class V_BorrowOrReturnBook:

    def __init__(self,type):                #type等于0为借书，type等于1为还书
        self.__root = Tk()
        self.__type = type;
        if type==0:
            self.__root.title("借书")
        elif type ==1:
           self.__root.title("还书")
        self.__root.geometry('420x70')  # 借书窗口起始

        frm = Frame(self.__root)  # 主界面起始
        frm_F = Frame(frm)  # 第一层起始

        frm_FL = Frame(frm_F)  # 第一层左起始
        Label(frm_FL, text='书籍号', font=('Arial', 12)).pack(side=TOP)
        frm_FL.pack(side=LEFT)  # 第一层左放置

        frm_FR = Frame(frm_F)  # 第一层右起始
        var_isbn = StringVar()
        self.__entryISBN = Entry(frm_FR, textvariable=var_isbn, width=30, font=('Verdana', 15))
        self.__entryISBN.pack()
        frm_FR.pack(side=RIGHT)  # 第一层右结束

        frm_F.pack(side=TOP)  # 第一层放置

        frm_S = Frame(frm)  # 第二层起始
        Button(frm_S, text="确认", command=self.ensure, width=6, height=1, font=('Arial', 10)).pack(side=LEFT)
        Button(frm_S, text="返回", command=self.__root.quit,width=6, height=1, font=('Arial', 10)).pack(side=RIGHT)
        frm_S.pack(side=BOTTOM)  # 第二层结束

        frm.pack()  # 主界面结束
        self.__root.mainloop()

    def ensure(self):
        isbn=self.__entryISBN.get()
        if self.__type == 0:
            1
            #借书控制层书籍信息操作
        elif self.__type == 1:
            1
            #还书控制层书籍信息操作

        if 1:       #操作成功
            a = tkinter.messagebox.showinfo('提示', '借书成功')
        else:       #操作失败
            a = tkinter.messagebox.showerror('错误', '借书失败')

a= V_BorrowOrReturnBook(1)