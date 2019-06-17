from tkinter import *
from tkinter import ttk

class V_SearchReader:

    def __init__(self,father):
        self.father = father
        self.root = Tk()
        self.root.title('SearchReader')
        self.root.geometry('400x420')
        self.root.geometry(self.father.locate)
        self.root.resizable(0,0)

        frameLine = Frame(self.root)
        frameLine.pack(side=TOP, ipadx=20)
        frameTreeView = Frame(self.root)
        frameTreeView.pack(side=TOP)

        labelReaderNumber = Label(frameLine, text='Input reader number:')
        self.__stringVarReaderNumber = StringVar()
        entryReaderNumber = Entry(frameLine, textvariable = self.__stringVarReaderNumber)
        buttonSearch = Button(frameLine, text='查询')
        buttonCancel = Button(frameLine, text='返回', command = self.returnFather)
        labelReaderNumber.pack(side = LEFT)
        entryReaderNumber.pack(side = LEFT)
        buttonSearch.pack(side = LEFT)
        buttonCancel.pack(side = LEFT)

        columns = ("读者号", "姓名", "联系方式", "是否逾期")
        tv = ttk.Treeview(frameTreeView, height=18, show="headings", columns=columns)

        tv.column("读者号", width=90, anchor='center')
        tv.column("姓名", width=100, anchor='center')
        tv.column("联系方式", width=100, anchor='center')
        tv.column("是否逾期", width=100, anchor='center')

        tv.heading("读者号", text="读者号")  # 显示表头
        tv.heading("姓名", text="姓名")
        tv.heading("联系方式", text="联系方式")
        tv.heading("是否逾期", text="是否逾期")

        tv.grid(row=1, columnspan=6, padx=1, pady=1)

        mainloop()

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()