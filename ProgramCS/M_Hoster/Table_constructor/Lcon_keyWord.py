
class Lcon_keyWord:
    def add(self,keyWordContext):
        self.sql = ''
        self.sql += "insert into t_keyword set keyWordContext = "
        self.sql += "'" + keyWordContext + "'"
        return self.sql

    def delete(self,keyWordId):
        self.sql = ''
        self.sql += "delete from t_keyword where "
        self.sql += "keyWordId = '" + keyWordId + "'"
        return self.sql
