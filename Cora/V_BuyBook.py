from tkinter import *
from PIL import Image, ImageTk
import qrcode
import time
from C_BuyBook import C_BuyBook
from tkinter import messagebox

class V_BuyBook:
    def __init__(self):
        self.__root = Tk()              #创建顶级窗口
        self.__root.title('买书')       #设置窗口题目
        self.__root.geometry('400x200') #设置买书窗口大小
        self.__root.resizable(0, 0)     #不可重设窗口大小
        #self.__payCode = Image.open("bg.png")
        #self.__imagePay = ImageTk.PhotoImage(image=self.__payCode)
        self.__payCode = qrcode.make('success')
        self.__imagePay = ImageTk.PhotoImage(image=self.__payCode)

        frm = Frame(self.__root)

        frameLable = Frame(frm)                   #设置标签
        Label(frameLable, text = 'BOOKNUMBER').pack(side = TOP)
        frameLable.pack(side = LEFT)

        frameEntry = Frame(frm)                   #设置输入框
        self.__varBookId = StringVar()
        self.__entryBookId = Entry(frameEntry, textvariable = self.__varBookId, width = 40)
        self.__entryBookId.pack(side = LEFT)
        frameEntry.pack(side = RIGHT)

        frm.pack(side = TOP, anchor = CENTER)

        frameButton = Frame(self.__root)          #设置按钮
        Button(frameButton, text = '购买', command = self.payBook, width = 6, height = 1).pack(side = LEFT)     #弹出支付窗口
        Button(frameButton, text = '取消', command = self.__root.quit, width = 6, height = 1).pack(side = LEFT) #返回
        frameButton.pack(anchor = CENTER)

        mainloop()

    # 创建付款子窗口
    def payBook(self):
        top = Toplevel()             #创建顶级窗口
        top.title('支付')
        top.geometry('400x400')
        top.resizable(0, 0)  # 不可重设窗口大小
        msg = Message(top, text = '请扫描二维码付款', width = 100).pack(anchor = CENTER)
        Label(top, image = self.__imagePay).pack(anchor = CENTER)

        frameButton = Frame(top)
        Button(frameButton, text = '我已付款', command = self.resultOfBuy, width = 6, height = 1).pack(side = LEFT)     #支付成功
        Button(frameButton, text = '放弃购买', command = top.quit, width = 6, height = 1).pack(side = LEFT)
        frameButton.pack(anchor = CENTER)

    def getBookId(self):
        return self.__varBookId.get()

    def resultOfBuy(self):
        # top = Toplevel()  # 创建顶级窗口
        # top.title('购买结果')
        # top.geometry('400x200')
        # top.resizable(0, 0)  # 不可重设窗口大小
        buyBook = C_BuyBook(self.getBookId())

        if buyBook.sendMessage():
            messagebox.showinfo('购买成功', '购买成功，谢谢惠顾。')
            self.__root.quit()
            self.__root.destroy()
        else:
            messagebox.showwarning('购买失败', '请去前台处理。')
            self.__root.quit()
            self.__root.destroy()

if __name__ == '__main__':
    v = V_BuyBook()


