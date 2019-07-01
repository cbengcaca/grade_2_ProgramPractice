class T_shelflocate:
    def add(self,shelfID,locate):
        sql = "insert into t_shelflocate(shelfId,shelflocate) values('"+shelfID+"','"+locate+"');"
        return sql
    def dele(self,shelfID):
        sql = "delete from t_shelflocate where shelfId='" + shelfID + "'"
        return sql