from tkinter import *
from V_search.V_SearchMain import V_Search
from V_readerEntrance.V_ReaderEntrance import V_ReaderEntrance
from V_adminEntrance.V_AdminEntrance import V_AdminEntrance
import _winapi
import win32gui,win32con


class V_Home():
    def __init__(self):
        self.size = '450x250'
        self.locate = '+200+200'
        self.root = Tk()
        self.root.title('HOME')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)


        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonSearch = Button(self.root,text = 'SEARCH BOOK',command = self.openSearchEntrance,font = 'Consoles')
        buttonSearch.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        buttonReader = Button(self.root,text = 'READER ENTRANCE',command = self.openReaderWindow,font = 'Consoles')
        buttonReader.pack(side = TOP)

        labelBlank3 = Label(self.root)
        labelBlank3.pack(side = TOP)

        buttonAdmin = Button(self.root,text = 'ADMIN ENTRANCE',command = self.openAdminWindow,font = 'Consoles')
        buttonAdmin.pack(side = TOP)

        mainloop()


    def openSearchEntrance(self):
        self.hideThisWindow()
        searchEntrance = V_Search(self)
        return

    def openReaderWindow(self):
        self.hideThisWindow()
        readerEntrance = V_ReaderEntrance(self)
        return

    def openAdminWindow(self):
        self.hideThisWindow()
        adminEntrance = V_AdminEntrance(self)
        return

#win32
    def getWindowHandle(self):
        return win32gui.FindWindow(None, self.root.title())

    def showThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(), win32con.SW_SHOW)

    def hideThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(), win32con.SW_HIDE)


a = V_Home()