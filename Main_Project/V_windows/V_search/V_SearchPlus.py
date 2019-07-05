from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from VC_windowsControl.VC_SearchPlus import VC_SearchPlus

class V_SearchPlus():

    def __init__(self):         #,father):
        # self.father = father
        self.root = Toplevel()
        self.root.title('SEARCHPLUS')
        self.root.geometry('400x300')
        # self.root.geometry(self.father.locate)
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

        labelRule1 = Label(frameLeft,text = 'Book Name')
        labelRule1.pack(side = TOP)
        self.bookName = StringVar()
        entryInput1 = Entry(frameLeft, textvariable=self.bookName)
        entryInput1.pack(side=TOP)

        labelRule2 = Label(frameRight, text='Author')
        labelRule2.pack(side = TOP)
        self.author = StringVar()
        entryInput2 = Entry(frameRight, textvariable = self.author)
        entryInput2.pack(side = TOP)

        labelRule3 = Label(frameLeft, text='Price Range')
        labelRule3.pack(side=TOP)
        self.Price = StringVar()
        entryInput3 = ttk.Combobox(frameLeft, width=17, textvariable = self.Price, state='readonly')
        entryInput3['values'] = ('', '50以下', '50-100', '100-150', '150-200', '200以上')
        entryInput3.pack(side = TOP)

        labelRule4 = Label(frameRight, text='Publish Time')
        labelRule4.pack(side=TOP)
        self.bookPublishTime = StringVar()
        entryInput4 = ttk.Combobox(frameRight, width=17, textvariable = self.bookPublishTime, state='readonly')
        entryInput4['values'] = ('',1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983
                                 , 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998
                                 , 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013
                                 , 2014, 2015, 2016, 2017, 2018, 2019)
        entryInput4.pack(side=TOP)

        labelRule5 = Label(frameLeft, text='Publisher')
        labelRule5.pack(side=TOP)
        self.bookPublisher = StringVar()
        entryInput5 = Entry(frameLeft, textvariable = self.bookPublisher)
        entryInput5.pack(side=TOP)

        labelRule6 = Label(frameRight, text='Sort Way')
        labelRule6.pack(side=TOP)
        self.sort = StringVar()
        entryInput6 = ttk.Combobox(frameRight, width=17, textvariable = self.sort, state='readonly')
        entryInput6['values'] = ('', '按书名升序', '按书名降序', '按价格升序', '按价格降序', '按销量升序', '按销量降序')
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
        self.root.quit()
        self.root.destroy()

    def getValue(self):

        if (self.bookName.get() == ''):
            self.bookName.set('None')

        if (self.author.get() == ''):
            self.author.set('None')

        if (self.Price.get() == ''):
            self.Price.set('None')         #############################################################################################################################################
            self.minPrice = 'None'
            self.maxPrice = 'None'
        elif (self.Price.get() == '50以下'):
            self.minPrice = 0
            self.maxPrice = 50
        elif (self.Price.get() == '50-100'):
            self.minPrice = 50
            self.maxPrice = 100
        elif (self.Price.get() == '100-150'):
            self.minPrice = 100
            self.maxPrice = 150
        elif (self.Price.get() == '150-200'):
            self.minPrice = 150
            self.maxPrice = 200
        else:
            self.minPrice = 200
            self.maxPrice = 999999

        if (self.bookPublishTime.get() == ''):
                self.bookPublishTime.set('None')

        if (self.bookPublisher.get() == ''):
                self.bookPublisher.set('None')
        #############################################################################################################################################
        if(self.sort.get() == ''):
            self.sort.set('None')
            self.sortValue = 'None'
            self.sortWay = 'None'
        elif (self.sort.get() == '按书名升序'):
            self.sortValue = '书名'
            self.sortWay = 1
        elif (self.sort.get() == '按书名降序'):
            self.sortValue = '书名'
            self.sortWay = 0
        elif(self.sort.get() == '按价格升序'):
            self.sortValue = '价格'
            self.sortWay = 1
        elif(self.sort.get() == '按价格降序'):
            self.sortValue = '价格'
            self.sortWay = 0
        elif(self.sort.get() == '按销量升序'):
            self.sortValue = '销量'
            self.sortWay = 1
        elif(self.sort.get() == '按销量降序'):
            self.sortValue = '销量'
            self.sortWay = 0


    def sendSearch(self):

        self.getValue()
        vc_searchPlus = VC_SearchPlus()
        searchList = ['1', str(self.bookName.get()), str(self.minPrice), str(self.maxPrice),str(self.bookPublishTime.get())
                        , str(self.author.get()), str(self.bookPublisher.get()),str(self.sortValue), str(self.sortWay), '==']
        vc_searchPlus.sendSearchToTcp(self, searchList)

        # bookList = [['bookName','bookPrice','bookCreateTime','bookAuthor','bookPublisher','bookSaleNumber','shelfLocate']]     ############

        # self.setBookInformation(bookList) ############


    def setBookInformation(self, bookList):
        if bookList:
            self.bookList = bookList
            self.showBookInformation()
        else:
            tkinter.messagebox.showwarning('警告', '无符合条件的书籍')

    def showBookInformation(self):
        searchResults = Tk()
        searchResults.title('SearchBook')
        searchResults.geometry('784x460')
        searchResults.resizable(0, 0)

        '''frameTop = Frame(searchResults)
        frameTop.pack(side=TOP)'''        #############################################################################################################################################
        frameTreeView = Frame(searchResults)
        frameTreeView.pack(side=TOP)
        frameReturn = Frame(searchResults)
        frameReturn.pack(side=TOP)

        '''labelInputTip = Label(frameTop, text='Double-click to view more')
        labelInputTip.pack(side=TOP)'''        #############################################################################################################################################

        columns = ("书名", "作者", "销量", "价格", "出版时间", "出版社", '可借时间', "所在书架" )
        tv = ttk.Treeview(frameTreeView, height=20, show="headings", columns=columns)

        tv.column("书名", width=150, anchor='center')
        tv.column("作者", width=120, anchor='center')
        tv.column("销量", width=40, anchor='center')
        tv.column("价格", width=50, anchor='center')
        tv.column("出版时间", width=60, anchor='center')
        tv.column("出版社", width=100, anchor='center')
        tv.column("可借时间", width=70, anchor='center')
        tv.column("所在书架", width=170, anchor='center')

        tv.heading("书名", text="书名")  # 显示表头
        tv.heading("作者", text="作者")
        tv.heading("销量", text="销量")
        tv.heading("价格", text="价格")
        tv.heading("出版时间", text="出版时间")
        tv.heading("出版社", text="出版社")
        tv.heading("可借时间", text="可借时间")
        tv.heading("所在书架", text="所在书架")

        def returnSearch():
            searchResults.quit()
            searchResults.destroy()

        buttonCancle = Button(frameReturn, text='RETURN', command=returnSearch)
        buttonCancle.pack(side=RIGHT)

        tv.grid(row=1, columnspan=6, padx=1, pady=1)

        k = 0
        for i in self.bookList:
            if(float(i[5]) > 0):
                tv.insert('', k, values=(i[0], i[3], i[6], i[1], i[2], i[4], '现在可借', i[7]))
            else:
                tv.insert('', k, values=(i[0], i[3], i[6], i[1], i[2], i[4], i[8], i[7]))
            k = k + 1

        #############################################################################################################################################
        # k = 0
        # for k in range (100):
        #     tv.insert('', k, values=(k, 2*k, 3*k, k-2, '套猴子', '套猴子', '我套屎你个大猴子'))
        #     k = k + 1


        vbar = ttk.Scrollbar(frameTreeView, orient=VERTICAL, command = tv.yview)
        tv.configure(yscrollcommand =vbar.set)
        tv.grid(row=0)
        vbar.grid(row=0, column=6, sticky=(N,S))

        '''        #############################################################################################################################################

        def treeviewClick(event):

            #print('双击')
            jm = Tk()
            jm.title("BOOK INFORMATION")
            jm.geometry('400x100')


            #print("me=", type(me))



            jm1 = Frame(jm)
            jm1.pack(side=TOP)
            jm2 = Frame(jm)
            jm2.pack(side=TOP)

            columns = ("书名", "作者", "销量", "价格")
            tv1 = ttk.Treeview(jm, height=1, show="headings", columns=columns)

            tv1.column("书名", width=90, anchor='center')
            tv1.column("作者", width=100, anchor='center')
            tv1.column("销量", width=100, anchor='center')
            tv1.column("价格", width=100, anchor='center')

            tv1.heading("书名", text="书名")  # 显示表头
            tv1.heading("作者", text="作者")
            tv1.heading("销量", text="销量")
            tv1.heading("价格", text="价格")
            tv1.pack()

            k = 0
            tv1.insert('', k, values=(self.bookList[k][0], self.bookList[k][3], self.bookList[k][5], self.bookList[k][1]))
            columns = ("出版社", "出版时间", "所在书架")
            tv2 = ttk.Treeview(jm, height=1, show="headings", columns=columns)

            tv2.column("出版社", width=130, anchor='center')
            tv2.column("出版时间", width=100, anchor='center')
            tv2.column("所在书架", width=160, anchor='center')

            tv2.heading("出版社", text="出版社")  # 显示表头
            tv2.heading("出版时间", text="出版时间")
            tv2.heading("所在书架", text="所在书架")
            tv2.pack()

            tv2.insert('', k, values=(self.bookList[k][2], self.bookList[k][4], self.bookList[k][6]))

        tv.bind('<Double-1>', treeviewClick)         '''

        mainloop()

# a = V_SearchPlus()        #############################################################################################################################################

