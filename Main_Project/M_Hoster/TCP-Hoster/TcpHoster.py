from socket import *
from tkinter import *
from tkinter import messagebox
import threading

from M_Hoster.M_Control import MC_BorrowOrReturnBook
from M_Hoster.M_Control.MC_devideWords import MC_devideWords
from M_Hoster.M_Control.MC_upBook import MC_UpBook
from M_Hoster.M_Control.MC_adminLogin import MC_AdminLogin
from M_Hoster.M_Control.MC_searchReader import MC_SearchReader
from M_Hoster.M_Control import MC_SignIn
from M_Hoster.M_Control.MC_SearchBorrowMassage import MC_SearchBorrowMassage
from M_Hoster.M_Control.MC_SearchNormal import MC_SearchNormal
from M_Hoster.M_Control.MC_downBook import MC_downBook
from M_Hoster.M_Control.MC_BuyBook import MC_BuyBook
import time
class TcpHoster(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = True
        self.host = '10.236.248.106'
        self.port = 4700
        self.buf = 1024
        self.addr = (self.host, self.port)


    def run(self):
        s = socket(AF_INET, SOCK_STREAM, 0)
        s.bind(self.addr)
        s.listen(5)

        while(True):  #用于强迫 发生错误之后，重新进入等待连接状态
            try:
                while self.flag is not False:
                    print('等待连接...\r\n')
                    cs, caddr = s.accept()

                    if self.flag is False:
                        cs.close()
                        print('...服务器停止\r\n')
                        break
                    if caddr is not self.host:
                        print('...连接来自于:', caddr)
                        data = '欢迎你的到来！\r\n'
                        cs.sendall(bytes(data, 'utf-8'))

                    recKeyWords = []
                    while True:
                        data = cs.recv(self.buf).decode('utf-8')
                        print(data)
                        if data == '==':
                            break
                        recKeyWords.append(data)
                    print(recKeyWords)
################主页查书
                    if recKeyWords[0] == '1': #主页查书
                        searchRec = MC_devideWords()
                        ret = searchRec.devideWords(recKeyWords[1:])
                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)
################主页查书
################买书
                    #'2'
                    #'34'
                    #'0'|'1'
                    if recKeyWords[0] == '2': #买书
                        buyBookId = recKeyWords[1]  #书籍Id
                        payFlag = recKeyWords[2]    #付款标志
                        buyBookRec = MC_BuyBook(buyBookId, payFlag)
                        ret = buyBookRec.buybook()

                        if ret == '0':
                            buyRecData = '1'     #标志购买成功
                            cs.sendall(bytes(buyRecData, 'utf-8'))
                            time.sleep(0.1)
                        elif ret == '-1':
                            buyRecData = '-1'     #标志已经付款了，但数据库操作失败
                            cs.sendall(bytes(buyRecData, 'utf-8'))
                            time.sleep(0.1)
                        elif ret == '2':
                            buyRecData = '0'  #标志界面中的书籍ID有误
                            cs.sendall(bytes(buyRecData, 'utf-8'))
                            time.sleep(0.1)
                        else:
                            buyRecData = '2'  # 已查找对应书籍，但未付款
                            cs.sendall(bytes(buyRecData, 'utf-8'))
                            time.sleep(0.5)
################买书毕

################借书
                    elif recKeyWords[0] == '3':
                        a = MC_BorrowOrReturnBook.MC_BorrowOrReturnBook()
                        result = []
                        result.append(str(a.Borrow(recKeyWords[1],recKeyWords[2])))
                        result.append("==")
                        for i in result:
                            if i == "==":
                                break
                            cs.sendall(bytes(i,'utf-8'))
################上架
                    elif recKeyWords[0] == '4':
                        bookUper = MC_UpBook()
                        ret = bookUper.searchIfIsbnExist(recKeyWords)

                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)

                        else:
                            cs.sendall(bytes("1", 'utf-8'))
                    ###isbn已存在
                    elif recKeyWords[0] == '4.1':
                        bookUper = MC_UpBook()
                        bookId = bookUper.addNewBook_exist(recKeyWords[1:])
                        cs.sendall(bytes(bookId, 'utf-8'))
                        time.sleep(0.5)

                    ###isbn不存在
                    elif recKeyWords[0] == '4.0':
                        bookUper = MC_UpBook()
                        bookId = bookUper.addNewBook_notexist(recKeyWords[1:])
                        cs.sendall(bytes(bookId, 'utf-8'))
                        time.sleep(0.5)
################上架毕
################下架
                    elif recKeyWords[0] == '5':
                        bookDown = MC_downBook()
                        ret = bookDown.changeBookInfo(recKeyWords)

                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)

                        else:
                            cs.sendall(bytes("1", 'utf-8'))
                    ################下架毕

                    ################查读
                    if recKeyWords[0] == '6':
                        searchReader = MC_SearchReader()
                        ret = searchReader.searchReader()
                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)
                        else:
                            cs.sendall(bytes('0', 'utf-8'))
                            time.sleep(0.1)
################查读毕

################查借阅7
                    if recKeyWords[0] == '7':
                        searchBorrow = MC_SearchBorrowMassage()
                        ret = searchBorrow.getSearchBorrow()
                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)

################查书normal8
                    if recKeyWords[0] == '8':
                        searchNormal = MC_SearchNormal()
                        ret = searchNormal.getSearchNormal(recKeyWords[1:])
                        if ret:
                            for singleLine in ret:
                                print(singleLine)
                                singleLineChangeToStr = ','.join([str(i) for i in singleLine])
                                print(singleLineChangeToStr)
                                cs.sendall(bytes(singleLineChangeToStr, 'utf-8'))
                                time.sleep(0.1)


################还书
                    elif recKeyWords[0] == '9':
                        a = MC_BorrowOrReturnBook.MC_BorrowOrReturnBook()
                        result = []
                        result.append(str(a.Return(recKeyWords[1])))
                        result.append("==")
                        for i in result:
                            if i == "==":
                                break
                            cs.sendall(bytes(i, 'utf-8'))

################登录
                    elif recKeyWords[0] == '10':
                        a = MC_SignIn.MC_SignIn()
                        result = []
                        result.append(str(a.sign(recKeyWords[1],recKeyWords[2])))
                        result.append("==")
                        for i in result:
                            if i == "==":
                                break
                            cs.sendall(bytes(i,'utf-8'))
################管理员登录
                    elif recKeyWords[0] == '11':
                        adminLoger = MC_AdminLogin()
                        ret = adminLoger.beginCompare(recKeyWords[1:])
                        cs.sendall(bytes(ret,'utf-8'))
                        time.sleep(0.1)

################管理员登录毕
                    time.sleep(0.1)
                    cs.sendall(bytes('==', 'utf-8'))
                    cs.close()
                    break
            except Exception as e:
                messagebox.showerror('ERROR','Something bad happen\nTcp Server is restarting')


    def stopThread(self):
        self.flag = False
        return

class hosterCtrl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.hoster = None

        self.root = Tk()
        self.root.geometry('400x200')
        self.root.geometry('+500+200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonStartThread = Button(self.root,text = 'START HOSTER',font = 'Consoles',command = self.startHoster)
        buttonStartThread.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        buttonEndThread = Button(self.root ,text = 'END HOSTER',font = 'Consoles',command = self.stopHoster)
        buttonEndThread.pack(side = TOP)

        labelBlank3 = Label(self.root)
        labelBlank3.pack(side = TOP)

        buttonCloseSystem = Button(self.root,text = 'END THIS SYSTEM',font = 'Consoles',command = self.closeSystem)
        buttonCloseSystem.pack(side = TOP)

        mainloop()

    def startHoster(self):
        if self.hoster is not None:
            messagebox.showwarning('tip', 'Hoster is already start')
        else:
            self.hoster = TcpHoster()
            self.hoster.start()
            messagebox.showinfo('tip', 'Hoster is start')

    def stopHoster(self):
        if self.hoster is None:
            messagebox.showwarning('tip', 'Hoster is already stop')

        else:
            self.hoster.stopThread()
            addr = (self.hoster.host, self.hoster.port)
            cs = socket(AF_INET, SOCK_STREAM, 0)
            cs.connect(addr)
            self.hoster = None
            messagebox.showinfo('tip', 'Hoster is stop')

    def closeSystem(self):
        if self.hoster is not None:
            messagebox.showwarning('tip', 'Hoster is not stop')
        else:
            messagebox.showinfo('tip', 'System will close soon')
            self.root.destroy()

T_hosterCtrl = hosterCtrl()
T_hosterCtrl.start()