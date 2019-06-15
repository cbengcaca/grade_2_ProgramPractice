from tkinter import *
from PIL import Image, ImageTk
import qrcode


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
        Label(frameLable, text = 'ISBN').pack(side = TOP)
        frameLable.pack(side = LEFT)

        frameEntry = Frame(frm)                   #设置输入框
        varISBN = StringVar()
        self.__entryISBN = Entry(frameEntry, textvariable = varISBN, width = 40)
        self.__entryISBN.pack(side = LEFT)
        frameEntry.pack(side = RIGHT)

        frm.pack(side = TOP, anchor = CENTER)

        frameButton = Frame(self.__root)          #设置按钮
        Button(frameButton, text = '购买', command = self.payBook, width = 6, height = 1).pack(side = LEFT)     #弹出支付窗口
        Button(frameButton, text = '取消', command = self.__root.quit, width = 6, height = 1).pack(side = LEFT) #返回
        frameButton.pack(anchor = CENTER)

        mainloop()

    def payBook(self):

        top = Toplevel()
        top.title('支付')

        Label(top, image = self.__imagePay).pack(anchor = CENTER)

if __name__ == '__main__':
    v=V_BuyBook()

