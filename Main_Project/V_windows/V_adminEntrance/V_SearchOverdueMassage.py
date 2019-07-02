from tkinter import *
from tkinter import ttk

class V_SearchOverdueMassage:

    def __init__(self):
        self.locate = '+400+200'
        self.root = Tk()
        self.root.title('SearchBorrowMassage')
        self.root.geometry('400x420')
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        frameTreeView = Frame(self.root)
        frameTreeView.pack(side=TOP)
        frameLine = Frame(self.root)
        frameLine.pack(side=TOP, ipadx=20)

        buttonSearch = Button(frameLine, text='下一页')
        buttonCancel = Button(frameLine, text='返回', command = self.returnFather)
        buttonCancel.pack(side = RIGHT)
        buttonSearch.pack(side = RIGHT)

        columns = ("借单号", "姓名", "联系方式", "超期时长")
        tv = ttk.Treeview(frameTreeView, height=18, show="headings", columns=columns)

        tv.column("借单号", width=90, anchor='center')
        tv.column("姓名", width=100, anchor='center')
        tv.column("联系方式", width=100, anchor='center')
        tv.column("超期时长", width=100, anchor='center')

        tv.heading("借单号", text="借单号")  # 显示表头
        tv.heading("姓名", text="姓名")
        tv.heading("联系方式", text="联系方式")
        tv.heading("超期时长", text="超期时长")

        tv.grid(row=1, columnspan=6, padx=1, pady=1)

        mainloop()

    def returnFather(self):
        self.root.quit()
        self.root.destroy()