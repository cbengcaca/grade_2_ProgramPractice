
class Acon_SearchBorrowMassage:

    #查询借单
    def setSearch(self):
        self.__selSQL = "SELECT * from v_borrowandreaderinfo"
        return self.__selSQL