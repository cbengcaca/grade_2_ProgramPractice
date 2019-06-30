from socket import *
from tkinter import *
from tkinter import messagebox
import threading
from M_Hoster.M_Control.MC_devideWords import MC_devideWords
import time
class TcpHoster(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = True
        self.host = '192.168.43.125'
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
################主页查书毕
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