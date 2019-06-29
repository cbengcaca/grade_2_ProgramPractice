
class LM_opOnISBNInfo:
    def add(self,bookName,bookAuthor,bookPublisher,bookPrice,bookCreateTime,bookMaxNum,bookAviliableNum,bookSaleNumber):
        self.sql = ''
        self.sql += "insert into t_isbninfo set "
        self.sql += "bookName = '" + bookName + "'"
        self.sql += ",bookAuthor = '" + bookAuthor + "'"
        self.sql += ",bookPulisher = '" + bookPublisher + "'"
        self.sql += ",bookPrice = '" + bookPrice + "'"
        self.sql += ",bookCreateTime = '" + bookCreateTime + "'"
        self.sql += ",bookMaxNum = '" + bookMaxNum + "'"
        self.sql += ",bookAviliable = '" + bookAviliableNum + "'"
        self.sql += ",bookSaleNumber = '" + bookSaleNumber + "'"
        return self.sql

    def delete(self,isbn):
        self.sql = ''
        self.sql += "delete from t_isbninfo where isbn = "
        self.sql += "'" + isbn + "'"
        return self.sql
