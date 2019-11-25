from tkinter import *
from PIL import Image, ImageTk
import qrcode
import time
from VC_windowsControl.VC_BuyBook import VC_BuyBook
from tkinter import messagebox

class V_BuyBook:
    def __init__(self):
        self.__root = Toplevel()              #创建顶级窗口
        self.__root.title('买书')       #设置窗口题目
        self.__root.geometry('400x200') #设置买书窗口大小
        self.__root.geometry('+420+300')
        self.__root.resizable(0, 0)     #不可重设窗口大小
        #self.__payCode = Image.open("bg.png")
        #self.__imagePay = ImageTk.PhotoImage(image=self.__payCode)
        self.__payCode = qrcode.make('success')
        self.__imagePay = ImageTk.PhotoImage(image=self.__payCode)
        frm = Frame(self.__root)

        frameLable = Frame(frm)                   #设置标签
        Label(frameLable, text = '书籍ID：', font = 'Consoles').pack(side = TOP)
        frameLable.pack(side = LEFT)

        frameEntry = Frame(frm)                   #设置输入框
        self.__varBookId = StringVar()
        self.__entryBookId = Entry(frameEntry, textvariable = self.__varBookId, width = 40)
        self.__entryBookId.pack(side = LEFT)
        frameEntry.pack(side = RIGHT)

        frm.pack(side = TOP, anchor = CENTER)

        frameButton = Frame(self.__root)          #设置按钮
        Button(frameButton, text = '购买', command = self.payBook, width = 6, height = 1,font = 'Consoles').pack(side = LEFT)       #支付界面
        Button(frameButton, text = '取消', command = self.selfRootDestory, width = 6, height = 1,font = 'Consoles').pack(side = LEFT)   #返回
        frameButton.pack(anchor = CENTER)

        mainloop()

    # 创建付款子窗口
    def payBook(self):
        # top = Toplevel()             #创建顶级窗口
        # top.title('支付')
        # top.geometry('400x400')
        # top.resizable(0, 0)  # 不可重设窗口大小
        buyBook = VC_BuyBook()
        if self.getBookId().isdigit():
            ret = buyBook.sendBuyMessage(self.getBookId(), 0)
            if ret == '2':
                self.second = Toplevel()
                msg = Message(self.second, text = '请扫描二维码付款', width = 100).pack(anchor = CENTER)
                Label(self.second, image = self.__imagePay).pack(anchor = CENTER)

                frameButton = Frame(self.second)
                Button(frameButton, text = '我已付款', command = self.resultOfBuy, width = 6, height = 1,font = 'Consoles').pack(side = LEFT)     #支付成功
                Button(frameButton, text = '放弃购买', command = self.selfDestory, width = 6, height = 1,font = 'Consoles').pack(side = LEFT)
                frameButton.pack(anchor = CENTER)
            else:
                messagebox.showwarning('错误', '书籍Id有误')
                self.__root.quit()
                self.__root.destroy()
        else:
            messagebox.showwarning('错误', '书籍Id有误')
            self.__root.quit()
            self.__root.destroy()

    def selfRootDestory(self):
        self.__root.quit()
        self.__root.destroy()

    def selfDestory(self):
        self.second.quit()
        self.second.destroy()

    def getBookId(self):
        return self.__varBookId.get()

    def resultOfBuy(self):
        payBook = VC_BuyBook()
        if payBook.sendBuyMessage(self.getBookId(), 1) == '1':
            messagebox.showinfo('购买成功', '购买成功，谢谢惠顾。')
            self.second.quit()
            self.second.destroy()
            self.__root.quit()
            self.__root.destroy()
        if payBook.sendBuyMessage(self.getBookId(), 1) == '-1':
            messagebox.showwarning('购买失败', '请去前台处理。')
            self.second.quit()
            self.second.destroy()
            self.__root.quit()
            self.__root.destroy()
        self.second.quit()
        self.second.destroy()

if __name__ == '__main__':
    v = V_BuyBook()


