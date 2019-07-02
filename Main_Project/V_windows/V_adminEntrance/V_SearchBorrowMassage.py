from tkinter import *
from tkinter import ttk
import tkinter.messagebox #弹窗库
import datetime
from VC_windowsControl.VC_SearchBorrowMassage import VC_SearchBorrowMassage

class V_SearchBorrowMassage:

    def __init__(self):#,father):
        self.getBorrowList()
        if self.borrowList:
            self.getTreeView()
        else:
            tkinter.messagebox.showinfo('提示', '无借单信息')

    def getTreeView(self):
        #self.father = father
        self.root = Tk()
        self.root.title('SearchBorrowMassage')
        self.root.geometry('714x460')
        # self.root.geometry(self.father.locate)
        self.root.resizable(0,0)

        frameTreeView = Frame(self.root)
        frameTreeView.pack(side=TOP)
        frameLine = Frame(self.root)
        frameLine.pack(side=TOP, ipadx=20)

        # labelBorrowMassageNumber = Label(frameLine, text='Input borrow number:')
        # self.__stringVarBorrowMassageNumber = StringVar()
        # entryBorrowMassageNumber = Entry(frameLine, textvariable = self.__stringVarBorrowMassageNumber)
        # labelBorrowMassageNumber.pack(side = LEFT)
        # entryBorrowMassageNumber.pack(side = LEFT)

        columns = ("借单号", "书籍ID", "借阅时间", "归还时间", "借阅者姓名", "信用积分", "借阅者联系方式")
        tv = ttk.Treeview(frameTreeView, height=20, show="headings", columns=columns)

        tv.column("借单号", width=80, anchor='center')
        tv.column("书籍ID", width=70, anchor='center')
        tv.column("借阅时间", width=130, anchor='center')
        tv.column("归还时间", width=130, anchor='center')
        tv.column("借阅者姓名", width=80, anchor='center')
        tv.column("信用积分", width=100, anchor='center')
        tv.column("借阅者联系方式", width=100, anchor='center')

        tv.heading("借单号", text="借单号")  # 显示表头
        tv.heading("书籍ID", text="书籍ID")
        tv.heading("借阅时间", text="借阅时间")
        tv.heading("归还时间", text="归还时间")
        tv.heading("借阅者姓名", text="借阅者姓名")
        tv.heading("信用积分", text="信用积分")
        tv.heading("借阅者联系方式", text="借阅者联系方式")

        tv.grid(row=1, columnspan=6, padx=1, pady=1)

        k = 0
        for i in self.borrowList:
            tv.insert('', k, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            k = k + 1

        vbar = ttk.Scrollbar(frameTreeView, orient=VERTICAL, command=tv.yview)
        tv.configure(yscrollcommand=vbar.set)
        tv.grid(row=0)
        vbar.grid(row=0, column=6, sticky=(N, S))

        def searchOverdueList():
            self.searchOverdue(tv)

        buttonSearch = Button(frameLine, text='查询违规借单', command = searchOverdueList)
        buttonCancel = Button(frameLine, text='返回', command=self.returnFather)
        buttonSearch.pack(side=LEFT)
        buttonCancel.pack(side=LEFT)

        mainloop()


    def returnFather(self):
        self.root.quit()
        self.root.destroy()

    def getBorrowList(self):
        List = ['7','==']
        VC_searchBorrowMassage = VC_SearchBorrowMassage()
        self.borrowList = VC_searchBorrowMassage.getBorrowList(List)

    def searchOverdue(self,tree):
        k = 0
        x = 0
        List = [[]]
        thirty_days = datetime.timedelta(days=30)
        now = datetime.datetime.now()
        date =str(now - thirty_days)
        time1 = date[:4] + date[5:7] + date[8:10] + date[11:13] + date[14:16] + date[17:19]

        for i in self.borrowList:
            time2 = i[2][:4] + i[2][5:7] + i[2][8:10] + i[2][11:13] + i[2][14:16] + i[2][17:19]
            if(i[3] == 'None' and int(time2) - int(time1) < 0):
                List[x] = i
                x = x + 1
            k = k + 1

        if(x == 0):
            tkinter.messagebox.showinfo('提示', '无违规借单')
        else:
            self.delButton(tree)
            k = 0
            for i in List:
                tree.insert('', k, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                k = k + 1

    def delButton(self,tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)


#a = V_SearchBorrowMassage()
