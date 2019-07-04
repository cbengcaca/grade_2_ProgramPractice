from tkinter import *
from tkinter import messagebox
from VC_windowsControl.VC_UpBook import VC_UpBook
from V_windows.V_adminEntrance.V_getIsbn import V_getIsbn
from  tkinter import ttk
class V_UpBook():

    def __init__(self,id):
        self.locate = '+200+200'
        self.isbn = ''
        self.operId = id
        self.root = Toplevel()
        self.root.title('UpBook')
        self.root.geometry('500x600')
        self.root.geometry(self.locate)
        self.root.resizable(0, 0)
        self.ret = [[]]

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        self.tree = ttk.Treeview(self.root,show="headings",height = 100 ,columns = ("ShelfId","ShelfLocate") )
        self.tree.column("ShelfId", width=100,anchor='center')  # 表示列,不显示
        self.tree.column("ShelfLocate", width=100,anchor='center')

        self.tree.heading("ShelfId", text="ShelfId")  # 显示表头
        self.tree.heading("ShelfLocate", text="ShelfLocate")

        self.tree.pack(side = LEFT)

        labelInputTip = Label(self.root,text = 'Input Here:')
        labelInputTip.pack(side = TOP)

        self.stringName = StringVar()
        labelBookName = Label(self.root,text = 'BookName:')
        labelBookName.pack(side = TOP)
        entryInput1 = Entry(self.root,textvariable = self.stringName)
        entryInput1.pack(side = TOP)

        self.stringAuthor = StringVar()
        labelBookAuthor = Label(self.root, text='BookAuthor:')
        labelBookAuthor.pack(side=TOP)
        entryInput3 = Entry(self.root , textvariable = self.stringAuthor)
        entryInput3.pack(side=TOP)

        self.stringPublisher = StringVar()
        labelBookPublisher = Label(self.root, text='BookPublisher:')
        labelBookPublisher.pack(side=TOP)
        entryInput4 = Entry(self.root,textvariable = self.stringPublisher)
        entryInput4.pack(side=TOP)

        self.stringPrice = StringVar()
        labelBookPublisher = Label(self.root, text='BookPrice:')
        labelBookPublisher.pack(side=TOP)
        entryInput5 = Entry(self.root,textvariable = self.stringPrice)
        entryInput5.pack(side=TOP)

        self.stringCreateTime = StringVar()
        labelBookPublisher = Label(self.root, text='BookCreateTime:')
        labelBookPublisher.pack(side=TOP)
        entryInput6 = Entry(self.root,textvariable = self.stringCreateTime)
        entryInput6.pack(side=TOP)

        self.stringLocate = StringVar()
        labelBookLocation = Label(self.root,text = 'BookLocation:\nPlease devide by whiteSpace' )
        labelBookLocation.pack(side = TOP)
        entryInput7 = Entry(self.root,textvariable = self.stringLocate)
        entryInput7.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'Confirm',command = self.addNewBookNotExist)
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text = 'SearchIsbn',command = self.getIsbn)
        buttonCancle.pack(side = RIGHT)

        labelBlankLast = Label(self.root)
        labelBlankLast.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='RETURN', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()
        #
        # isbn = infoList[1]
        # bookName = infoList[2]
        # bookAuthor = infoList[3]
        # bookPublisher = infoList[4]
        # bookPrice = infoList[5]
        # bookCreateTime = infoList[6]
        # operId = infoList[7]
        # shelfId = infoList[8]

    def getIsbn(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        vc = VC_UpBook()
        getIsbn = V_getIsbn(self)
        if getIsbn == '':
            messagebox.showerror(message= '输入ISBN不能为空')
        infoList = ['4', self.isbn]
        #查询isbn是否存在
        #存在返回1
        #不存在返回书架信息
        ret = vc.searchIsbnExist(infoList)

        if ret is  '1':##isbn存在
            infoList = ['4.1', self.isbn, self.operId]
            ##获得最新的bookid
            bookId = vc.addBookExist(infoList)
            if bookId is not '0':
                messagebox.showinfo(message= '新书id为：'+ bookId)
            else:
                messagebox.showerror(message= '上架失败')
            return
        else: ##isbn不存在
            self.ret = ret
            for list in ret:
                self.setTreeView(list)

    def setIsbn(self,isbn):
        self.isbn = isbn

    def setTreeView(self,list):
        self.tree.insert('', 'end', values = list)

    def addNewBookNotExist(self):
        if self.ret == [[]]:
            messagebox.showerror(message= '没有事先查询ISBN信息')
            return





        infoList = ['4.0']
        infoList.append(self.isbn)
        infoList.append(self.stringName.get())
        infoList.append(self.stringAuthor.get())
        infoList.append(self.stringPublisher.get())
        infoList.append(self.stringPrice.get())
        infoList.append(self.stringCreateTime.get())
        infoList.append(self.operId)
        infoList.append(self.stringLocate.get())

        flag = True
        for i in infoList:
            if i == '':
                flag = False
        if flag == False:
            messagebox.showerror(message= '输入信息不完整')
            return

        flag = False
        for i in self.ret:
            if self.stringLocate.get() == i:
                flag = True
        if flag == False:
            messagebox.showerror(message= '书架信息有误')
            return

        vc = VC_UpBook()
        bookId = vc.addBookNotExist(infoList)
        if bookId is not '0':
            messagebox.showinfo(message='新书id是：' + bookId)
        else:
            messagebox.showerror(message='上架失败')

    def returnFather(self):
        self.root.quit()
        self.root.destroy()



