from tkinter import *
from tkinter import ttk
from VC_windowsControl.VC_SearchReader import VC_SearchReader
class V_SearchReader:

    def __init__(self):
        self.locate = '+400+200'
        self.root = Tk()
        self.root.title('SearchReader')
        self.root.geometry('500x420')
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        frameLine = Frame(self.root)
        frameLine.pack(side=TOP, ipadx=20)
        frameTreeView = Frame(self.root)
        frameTreeView.pack(side=TOP)

        columns = ("读者号", "姓名", "性别", "联系方式","信誉积分")
        self.tv = ttk.Treeview(frameTreeView, height=18, show="headings", columns=columns)

        self.tv.column("读者号", width=90, anchor='center')
        self.tv.column("姓名", width=100, anchor='center')
        self.tv.column("性别", width=100, anchor='center')
        self.tv.column("联系方式", width=100, anchor='center')
        self.tv.column("信誉积分", width=100, anchor='center')

        self.tv.heading("读者号", text="读者号")  # 显示表头
        self.tv.heading("姓名", text="姓名")
        self.tv.heading("性别", text="性别")
        self.tv.heading("联系方式", text="联系方式")
        self.tv.heading("信誉积分", text="信誉积分")

        self.tv.grid(row=1, columnspan=6, padx=1, pady=1)

        self.beginSearch()
        mainloop()

    def beginSearch(self):
        vc = VC_SearchReader()
        ret = vc.beginSearchReader()
        for i in ret:
            self.setTreeView(i)

    def setTreeView(self,list):
        self.tv.insert('', 'end', values=list)

    def returnFather(self):
        self.root.quit()
        self.root.destroy()

