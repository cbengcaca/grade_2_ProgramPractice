from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from VC_windowsControl.VC_SearchNormal import VC_SearchNormal

class V_SearchNormal():
    def __init__(self):
        self.root = Toplevel()
        self.root.title('SEARCHNORMAL')
        self.root.geometry('400x300')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frame = Frame(self.root)
        frame.pack(side = TOP)
        labelInputTip = Label(frame,text = 'Select * from Table                                 ')
        labelInputTip.pack(side = TOP)
#书名
        frameName = Frame(self.root)
        frameName.pack(side = TOP)
        labelRule1 = Label(frameName, text='Where 书名=')
        labelRule1.pack(side=LEFT)

        self.bookName = StringVar()
        entryBookName = ttk.Combobox(frameName, width=20, textvariable=self.bookName)
        entryBookName['values'] = ('', '%JAVA%', '%Android%', '%高考%')
        entryBookName.pack(side=RIGHT)

#作者
        frameAuthor = Frame(self.root)
        frameAuthor.pack(side=TOP)
        labelRule2 = Label(frameAuthor, text='         作者 =')
        labelRule2.pack(side=LEFT)

        self.Author = StringVar()
        entryAuthor = ttk.Combobox(frameAuthor, width=20, textvariable=self.Author)
        entryAuthor['values'] = ('', '%欧阳燊%', '%周志明%', '%Robert%')
        entryAuthor.pack(side=RIGHT)

#价格
        frameMinPrice = Frame(self.root)
        frameMinPrice.pack(side=TOP)
        labelRule3 = Label(frameMinPrice, text='         价格 =')
        labelRule3.pack(side=LEFT)

        self.minPrice = StringVar()
        entryminPrice = ttk.Combobox(frameMinPrice, width=20, textvariable=self.minPrice)
        entryminPrice['values'] = ('', ' bookPrice >= 0  ')
        entryminPrice.pack(side=RIGHT)

        frameMaxPricemin = Frame(self.root)
        frameMaxPricemin.pack(side=TOP)
        labelRule4 = Label(frameMaxPricemin, text='         价格 =')
        labelRule4.pack(side=LEFT)

        self.maxPrice = StringVar()
        entrymaxPrice = ttk.Combobox(frameMaxPricemin, width=20, textvariable=self.maxPrice)
        entrymaxPrice['values'] = ('', ' bookPrice <= 50  ')
        entrymaxPrice.pack(side=RIGHT)

#出版时间
        framePublishTime = Frame(self.root)
        framePublishTime.pack(side=TOP)
        labelRule5 = Label(framePublishTime, text='   出版时间 =')
        labelRule5.pack(side=LEFT)

        self.publishTime = StringVar()
        entryPublishTime = ttk.Combobox(framePublishTime, width=20, textvariable=self.publishTime)
        entryPublishTime['values'] = ('', '2010', '2014', '2016', '2019')
        entryPublishTime.pack(side=RIGHT)

#出版社
        framePublisher = Frame(self.root)
        framePublisher.pack(side=TOP)
        labelRule6 = Label(framePublisher, text='      出版社 =')
        labelRule6.pack(side=LEFT)

        self.publisher = StringVar()
        entryPublisher = ttk.Combobox(framePublisher, width=20, textvariable=self.publisher)
        entryPublisher['values'] = ('', '%机械工业出版社%',  '%人民邮电出版社%', '%清华大学出版社%')
        entryPublisher.pack(side=RIGHT)

#排序方式
        frameSortWay = Frame(self.root)
        frameSortWay.pack(side=TOP)
        labelRule7 = Label(frameSortWay, text='   排序方式 =')
        labelRule7.pack(side=LEFT)

        self.sortWay = StringVar()
        entrySortWay = ttk.Combobox(frameSortWay, width=20, textvariable=self.sortWay, state='readonly')
        entrySortWay['values'] = ('',' ORDER BY bookName ', ' ORDER BY bookPrice ', ' ORDER BY bookSaleNumber ')
        entrySortWay.pack(side=RIGHT)

#升降序
        frameSort = Frame(self.root)
        frameSort.pack(side=TOP)
        labelRule8 = Label(frameSort, text='      升降序 =')
        labelRule8.pack(side=LEFT)

        self.sort = StringVar()
        entrySort = ttk.Combobox(frameSort, width=20, textvariable=self.sort, state='readonly')
        entrySort['values'] = ('',' ASC', ' DESC')
        entrySort.pack(side=RIGHT)
#按钮
        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle, text='CONFIRM', command=self.sendSearch)
        buttonConfirm.pack(side=LEFT)
        buttonCancle = Button(frameOkCancle, text='RETURN', command=self.returnFather)
        buttonCancle.pack(side=RIGHT)

        mainloop()

    def returnFather(self):
        self.root.quit()
        self.root.destroy()

    def getSql(self):
        self.selSQL = "SELECT a.bookName,a.bookPrice,a.bookCreateTime,a.bookAuthor, " \
                        "a.bookPUblisher,a.bookAvailableNum ,a.bookSaleNumber, b.shelflocate, date_format(b.returntime, '%Y%m%d')"
        self.selSQL += " from t_isbninfo a left join v_borrowandbookinfo b on a.isbn = b.isbn"
        flag = 0
        if self.bookName.get() != '':
            flag = 1
            self.selSQL += " Where "
            self.selSQL += " bookName LIKE '"
            self.selSQL += str(self.bookName.get())
            self.selSQL += "'"
        if self.Author.get() != '':
            if flag == 0:
                flag = 1
                self.selSQL += " Where "
            else:
                self.selSQL += " and "
            self.selSQL += " bookAuthor LIKE '"
            self.selSQL += str(self.Author.get())
            self.selSQL += "'"
        if self.minPrice.get() != '':
            if flag == 0 :
                flag = 1
                self.selSQL += " Where "
            else:
                self.selSQL += " and "
            self.selSQL += str(self.minPrice.get())
        if self.maxPrice.get() != '':
            if flag == 0 :
                flag = 1
                self.selSQL += " Where "
            else:
                self.selSQL += " and "
            self.selSQL += str(self.maxPrice.get())
        if self.publishTime.get() != '':
            if flag == 0:
                flag = 1
                self.selSQL += " Where "
            else:
                self.selSQL += " and "
            self.selSQL += " bookCreateTime = "
            self.selSQL += str(self.publishTime.get())
        if self.publisher.get() != '':
            if flag == 0:
                flag = 1
                self.selSQL += " Where "
            else:
                self.selSQL += " and "
            self.selSQL += " bookPublisher LIKE '"
            self.selSQL += str(self.publisher.get())
            self.selSQL += "'"
        if self.sortWay.get() != '':
            self.selSQL += str(self.sortWay.get())
        if self.sort.get() != '':
            self.selSQL += str(self.sort.get())



    def sendSearch(self):
        self.getSql()
        vc_searchNormal = VC_SearchNormal()
        searchList = ['8', self.selSQL, '==']
        vc_searchNormal.sendSearchToTcp(self, searchList)

    def setBookInformation(self, bookList):
        if bookList:
            if bookList == [['0']]:
                tkinter.messagebox.showwarning('警告', '输入了错误的SQL语句')
            else:
                self.bookList = bookList
                self.showBookInformation()
        else:
            tkinter.messagebox.showwarning('警告', '无符合条件的书籍')

    def showBookInformation(self):
        searchResults = Tk()
        searchResults.title('SearchBook')
        searchResults.geometry('784x460')
        searchResults.resizable(0, 0)

        frameTreeView = Frame(searchResults)
        frameTreeView.pack(side=TOP)
        frameReturn = Frame(searchResults)
        frameReturn.pack(side=TOP)

        columns = ("书名", "作者", "销量", "价格", "出版时间", "出版社", '可借时间', "所在书架")
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
            if (float(i[5]) > 0):
                tv.insert('', k, values=(i[0], i[3], i[6], i[1], i[2], i[4], '现在可借', i[7]))
            else:
                tv.insert('', k, values=(i[0], i[3], i[6], i[1], i[2], i[4], i[8], i[7]))
            k = k + 1

        vbar = ttk.Scrollbar(frameTreeView, orient=VERTICAL, command=tv.yview)
        tv.configure(yscrollcommand=vbar.set)
        tv.grid(row=0)
        vbar.grid(row=0, column=6, sticky=(N, S))

        mainloop()