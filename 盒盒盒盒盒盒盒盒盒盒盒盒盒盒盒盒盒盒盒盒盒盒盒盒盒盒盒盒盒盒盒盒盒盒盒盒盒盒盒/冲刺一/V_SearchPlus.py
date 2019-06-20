from tkinter import *
from tkinter import ttk

class V_SearchPlus():

    def __init__(self,father):
        self.father = father
        self.root = Tk()
        self.root.title('SEARCHPLUS')
        self.root.geometry('400x300')
        self.root.geometry(self.father.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = 'INPUT HERE:')
        labelInputTip.pack(side = TOP)

        frame = Frame(self.root)
        frame.pack()
        frameLeft = Frame(frame)
        frameLeft.pack(side = LEFT)
        frameRight = Frame(frame)
        frameRight.pack(side = RIGHT)

        labelRule1 = Label(frameLeft,text = 'BookName')
        labelRule1.pack(side = TOP)
        self.bookName = StringVar()
        entryInput1 = Entry(frameLeft, textvariable=self.bookName)
        entryInput1.pack(side=TOP)

        labelRule2 = Label(frameRight, text='Author')
        labelRule2.pack(side = TOP)
        self.author = StringVar()
        entryInput2 = Entry(frameRight, textvariable = self.author)
        entryInput2.pack(side = TOP)

        labelRule3 = Label(frameLeft,text = 'Min price')
        labelRule3.pack(side = TOP)
        self.minPrice = StringVar()
        entryInput3 = Entry(frameLeft, textvariable = self.minPrice)
        entryInput3.pack(side = TOP)

        labelRule4 = Label(frameRight, text='Max price')
        labelRule4.pack(side=TOP)
        self.maxPrice = StringVar()
        entryInput4 = Entry(frameRight, textvariable=self.maxPrice)
        entryInput4.pack(side=TOP)

        labelRule5 = Label(frameLeft, text='bookPublishTime')
        labelRule5.pack(side=TOP)
        self.bookPublishTime = StringVar()
        entryInput5 = Entry(frameLeft, textvariable=self.bookPublishTime)
        self.bookPublishTime.set('YYYY-MM')
        entryInput5.pack(side=TOP)

        labelRule6 = Label(frameRight, text='bookPublisher')
        labelRule6.pack(side=TOP)
        self.bookPublisher = StringVar()
        entryInput6 = Entry(frameRight, textvariable=self.bookPublisher)
        entryInput6.pack(side=TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)
        
        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'CONFIRM',command = self.sendSearch)
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text='RETURN', command=self.returnFather)
        buttonCancle.pack(side = RIGHT)

        mainloop()

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()

    def sendSearch(self):
        if(self.bookName.get() == ''):
            self.bookName.set(NONE)
        if (self.author.get() == ''):
            self.author.set(NONE)
        if(self.minPrice.get() == ''):
            self.minPrice.set(NONE)
        if(self.maxPrice.get() == ''):
            self.maxPrice.set(NONE)
        if(self.bookPublishTime.get() == ''):
            self.bookPublishTime.set(NONE)
        if(self.bookPublisher.get() == ''):
            self.bookPublisher.set(NONE)
        c_searchPlus = C_SearchPlus()
        searchList = [ 1, self.bookName.get(), self.minPrice.get(), self.maxPrice.get(), self.bookPublishTime.get(), self.author.get(), self.bookPublisher.get()]
        c_searchPlus.sendSearchToTcp(self, searchList)


    def setBookInformation(self, bookList):
        self.bookList = bookList
        self.showBookInformation()

    def showBookInformation(self):
        searchResults = Tk()
        searchResults.title('SearchBook')
        searchResults.geometry('400x280')
        searchResults.resizable(0, 0)

        frameTop = Frame(searchResults)
        frameTop.pack(side=TOP)
        frameTreeView = Frame(searchResults)
        frameTreeView.pack(side=TOP)
        frameReturn = Frame(searchResults)
        frameReturn.pack(side=TOP)

        labelInputTip = Label(frameTop, text='Double-click to view more')
        labelInputTip.pack(side=TOP)

        columns = ("书名", "作者", "剩余数量", "价格")
        tv = ttk.Treeview(frameTreeView, height=10, show="headings", columns=columns)

        tv.column("书名", width=90, anchor='center')
        tv.column("作者", width=100, anchor='center')
        tv.column("剩余数量", width=100, anchor='center')
        tv.column("价格", width=100, anchor='center')

        tv.heading("书名", text="书名")  # 显示表头
        tv.heading("作者", text="作者")
        tv.heading("剩余数量", text="剩余数量")
        tv.heading("价格", text="价格")

        Page = StringVar()
        labelPage = Label(frameReturn, text='page')
        labelPage.pack(side=LEFT)
        entryPage = Entry(frameReturn, textvariable=Page)
        entryPage.pack(side=LEFT)
        buttonGoPage = Button(frameReturn, text='GO THIS PAGE')
        buttonGoPage.pack(side=LEFT)
        buttonCancle = Button(frameReturn, text='RETURN')
        buttonCancle.pack(side=RIGHT)

        tv.grid(row=1, columnspan=6, padx=1, pady=1)

        k = 0
        for k in len(self.bookList):
            tv.insert('', k, values=(self.bookList[k][1], self.bookList[k][2], self.bookList[k][3], self.bookList[k][4]))
            #print(k)
            k = k + 1

        def treeviewClick(event):
            print('双击')
            jm = Tk()
            jm.title("BOOK INFORMATION")
            jm.geometry('400x100')

            jm1 = Frame(jm)
            jm1.pack(side=TOP)
            jm2 = Frame(jm)
            jm2.pack(side=TOP)

            columns = ("书名", "作者", "剩余数量", "价格")
            tv1 = ttk.Treeview(jm, height=1, show="headings", columns=columns)

            tv1.column("书名", width=90, anchor='center')
            tv1.column("作者", width=100, anchor='center')
            tv1.column("剩余数量", width=100, anchor='center')
            tv1.column("价格", width=100, anchor='center')

            tv1.heading("书名", text="书名")  # 显示表头
            tv1.heading("作者", text="作者")
            tv1.heading("剩余数量", text="剩余数量")
            tv1.heading("价格", text="价格")
            tv1.pack()

            k = 1
            tv1.insert('', k, values=(self.bookList[k][1], self.bookList[k][2], self.bookList[k][3], self.bookList[k][4]))

            columns = ("书名", "作者", "剩余数量", "价格")
            tv2 = ttk.Treeview(jm, height=1, show="headings", columns=columns)

            tv2.column("书名", width=90, anchor='center')
            tv2.column("作者", width=100, anchor='center')
            tv2.column("剩余数量", width=100, anchor='center')
            tv2.column("价格", width=100, anchor='center')

            tv2.heading("书名", text="书名")  # 显示表头
            tv2.heading("作者", text="作者")
            tv2.heading("剩余数量", text="剩余数量")
            tv2.heading("价格", text="价格")
            tv2.pack()

            tv2.insert('', k, values=(self.bookList[k][5], self.bookList[k][6], self.bookList[k][7], self.bookList[k][8]))

        tv.bind('<Double-1>', treeviewClick)

        mainloop()





#a = V_SearchPlus()