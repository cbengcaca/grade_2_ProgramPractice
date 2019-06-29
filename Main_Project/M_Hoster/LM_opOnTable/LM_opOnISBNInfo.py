import pymysql
from M_Hoster.LM_opOnTable.LM_superDBOp import LM_superDBOp
class LM_opOnISBNInfo(LM_superDBOp):
    def __init__(self):
        super(LM_opOnISBNInfo, self).__init__()

    def add(self,bookName,bookAuthor,bookPublisher,bookPrice,bookCreateTime,bookMaxNum,bookAviliableNum,bookSaleNumber):
        self.sql += "insert into t_isbninfo set "
        self.sql += "bookName = '" + bookName + "'"
        self.sql += ",bookAuthor = '" + bookAuthor + "'"
        self.sql += ",bookPulisher = '" + bookPublisher + "'"
        self.sql += ",bookPrice = '" + bookPrice + "'"
        self.sql += ",bookCreateTime = '" + bookCreateTime + "'"
        self.sql += ",bookMaxNum = '" + bookMaxNum + "'"
        self.sql += ",bookAviliable = '" + bookAviliableNum + "'"
        self.sql += ",bookSaleNumber = '" + bookSaleNumber + "'"

    def delete(self,isbn):
        self.sql += "delete from t_isbninfo where isbn = "
        self.sql += "'" + isbn + "'"



