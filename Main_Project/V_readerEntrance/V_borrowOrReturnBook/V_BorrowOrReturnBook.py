from tkinter import *
import tkinter.messagebox
from V_readerEntrance.V_borrowOrReturnBook.V_SignIn import V_SignIn


class V_BorrowOrReturnBook:

    def __init__(self,type,father):
        self.father = father
        self.status = 0
        k = V_SignIn(self,father)


        if(self.status):
            self.root = Tk()
            if (type == 0):
                self.root.title("借书")
            elif (type == 1):
                self.root.title("还书")
            self.root.geometry('420x70')  # 借书窗口起始
            self.root.geometry(self.father.locate)

            frm = Frame(self.root)                        # 主界面起始

            frm_F = Frame(frm)                                      # 第一层起始

            frm_FL = Frame(frm_F)                                           # 第一层左起始
            Label(frm_FL, text='书籍号', font=('Arial', 12)).pack(side=TOP)
            frm_FL.pack(side=LEFT)                                          # 第一层左放置

            frm_FR = Frame(frm_F)                                           # 第一层右起始
            var_isbn = StringVar()
            self.__entryISBN = Entry(frm_FR, textvariable=var_isbn, width=30, font=('Verdana', 15))
            self.__entryISBN.pack()
            frm_FR.pack(side=RIGHT)                                         # 第一层右结束

            frm_F.pack(side=TOP)                                    # 第一层放置

            frm_S = Frame(frm)                                      # 第二层起始
            if (type == 0):
                Button(frm_S, text="借书", command=lambda: self.ensure(0), width=6, height=1, font=('Arial', 10)).pack(
                    side=LEFT)
            elif (type == 1):
                Button(frm_S, text="还书", command=lambda: self.ensure(1), width=6, height=1, font=('Arial', 10)).pack(
                side=LEFT)
            Button(frm_S, text="返回", command=self.returnFather, width=6, height=1, font=('Arial', 10)).pack(side=RIGHT)
            frm_S.pack(side=BOTTOM)                                 # 第二层结束

            frm.pack()                                      # 主界面结束
            self.root.mainloop()
        else:
            self.returnFather()

    def ensure(self,type):
        isbn=self.__entryISBN.get()
        if type == 0:
            pass
            #借书控制层书籍信息操作
        elif type == 1:
            pass
            #还书控制层书籍信息操作

        if 1:       #操作成功
            a = tkinter.messagebox.showinfo('提示', '借书成功')
            self.__entryISBN.delete(0,END)
        else:       #操作失败
            a = tkinter.messagebox.showerror('错误', '借书失败')
#a = V_BorrowOrReturnBook(1)            #调用示例，当进入读者接口时调用

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()