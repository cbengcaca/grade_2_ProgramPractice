
class Lcon_opOnISBNInfo:
    def add(self,isbn,bookName,bookAuthor,bookPublisher,bookPrice,bookCreateTime,bookMaxNum,bookAviliableNum,bookSaleNumber):
        self.sql = ''
        self.sql += "insert into t_isbninfo set "
        self.sql += "isbn = '" + isbn + "'"
        self.sql += ",bookName = '" + bookName + "'"
        self.sql += ",bookAuthor = '" + bookAuthor + "'"
        self.sql += ",bookPublisher = '" + bookPublisher + "'"
        self.sql += ",bookPrice = '" + bookPrice + "'"
        self.sql += ",bookCreateTime = str_to_date('" + bookCreateTime + "', '%m/%d/%y')"
        self.sql += ",bookMaxNum = '" + bookMaxNum + "'"
        self.sql += ",bookAvailableNum = '" + bookAviliableNum + "'"
        self.sql += ",bookSaleNumber = '" + bookSaleNumber + "'"
        return self.sql

    def delete(self,isbn):
        self.sql = ''
        self.sql += "delete from t_isbninfo where isbn = "
        self.sql += "'" + isbn + "'"
        return self.sql
