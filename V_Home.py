from tkinter import *
from V_search.V_SearchMain import V_Search
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

        buttonReader = Button(frameButton,text = 'READER')
        buttonReader.pack(side = LEFT)

        buttonAdmin = Button(frameButton,text = 'ADMIN')
        buttonAdmin.pack(side = LEFT)

        mainloop()

    def openSearchEntrance(self):
        searchEntrance = V_Search()
        return

    def openReaderWindow(self):

        return

    def openAdminWindow(self):

        return

a = V_Home()