from tkinter import *
from V_search.V_SearchNormal import V_SearchNormal
from V_search.V_SearchPlus import V_SearchPlus
import win32con,win32gui
class V_Search():
    def __init__(self,father):
        self.father = father
        self.size = father.size
        self.locate = father.locate
        self.root = Tk()
        self.root.title('SEARCH')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frameSearchEntrance = Frame(self.root)
        frameSearchEntrance.pack(side = TOP)

        buttonSearchPlus = Button(frameSearchEntrance,text = 'SEARCHPLUS',command = self.openSearchPlus,font = 'Consoles')
        buttonSearchPlus.pack(side = LEFT)

        buttonSearchNormal = Button(frameSearchEntrance,text = 'SEARCHNORMAL',command = self.openSearchNormal,font = 'Consoles')
        buttonSearchNormal.pack(side = RIGHT)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = BOTTOM)

        buttonReturn = Button(self.root,text = 'RETURN',command = self.returnFather,font = 'Consoles')
        buttonReturn.pack(side = BOTTOM)
        mainloop()


    def openSearchPlus(self):
        self.hideThisWindow()
        V_searchPlusNew = V_SearchPlus(self)
        return

    def openSearchNormal(self):
        self.hideThisWindow()
        V_searchNormalNew = V_SearchNormal(self)
        return

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()

    def getWindowHandle(self):
        return win32gui.FindWindow(None,self.root.title())

    def showThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_SHOW)

    def hideThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_HIDE)




