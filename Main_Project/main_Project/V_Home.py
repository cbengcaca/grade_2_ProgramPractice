from tkinter import *
from .V_search.V_SearchMain import V_Search
from .V_readerEntrance.V_ReaderEntrance import V_ReaderEntrance
from .V_adminEntrance.V_AdminEntrance import V_AdminEntrance

class V_Home():
    def __init__(self):
        self.__root = Tk()
        self.__root.title('HOME')
        self.__root.geometry('400x200')
        self.__root.resizable(0,0)

        labelBlank1 = Label(self.__root)
        labelBlank1.pack(side = TOP)

        frameButton = Frame(self.__root)
        frameButton.pack(side = TOP)

        buttonSearch = Button(frameButton,text = 'SEARCH',command = self.openSearchEntrance)
        buttonSearch.pack(side = LEFT)

        buttonReader = Button(frameButton,text = 'READER',command = self.openReaderWindow)
        buttonReader.pack(side = LEFT)

        buttonAdmin = Button(frameButton,text = 'ADMIN',command = self.openAdminWindow)
        buttonAdmin.pack(side = LEFT)

        mainloop()

    def openSearchEntrance(self):
        searchEntrance = V_Search()
        return

    def openReaderWindow(self):
        readerEntrance = V_ReaderEntrance()
        return

    def openAdminWindow(self):
        adminEntrance = V_AdminEntrance()
        return

a = V_Home()