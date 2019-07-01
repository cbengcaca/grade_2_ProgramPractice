from socket import *
from tkinter import *
from tkinter import messagebox
import threading
from M_Hoster.M_Control.MC_devideWords import MC_devideWords
from M_Hoster.M_Control.MC_upBook import MC_UpBook
from M_Hoster.M_Control.MC_adminLogin import MC_AdminLogin
from M_Hoster.M_Control import MC_BorrowOrReturnBook
from M_Hoster.M_Control import MC_SignIn
import time
class TcpHoster(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = True
        self.host = '192.168.56.1'
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
                        if ret:  #isbn存在
                            print("isbn is exist")
                            cs.sendall(bytes("1",'utf-8'))
                        else:
                            print("isbn is not exist")
                            cs.sendall(bytes("0",'utf-8'))

                    elif recKeyWords[0] == '4.1':
                        bookUper = MC_UpBook()
                        ret = bookUper.addNewBook_exist(recKeyWords)

                    elif recKeyWords[0] == '4.0':
                        bookUper = MC_UpBook()
                        ret = bookUper.addNewBook_notexist(recKeyWords)
################上架毕

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