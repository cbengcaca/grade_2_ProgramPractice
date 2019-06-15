from tkinter import *

class V_ReaderEntrance():
    def __init__(self):
        self.root = Tk()
        self.root.title('READER ENTRANCE')
        self.root.geometry('400x200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonBuy = Button(self.root,text = 'BUYBOOK')
        buttonBuy.pack(side = TOP)


        buttonBorrow = Button(self.root,text = 'BORROWBOOK')
        buttonBorrow.pack(side = TOP)

        buttonReturn = Button(self.root,text = 'RETURNBOOK')
        buttonReturn.pack(side = TOP)

        mainloop()

