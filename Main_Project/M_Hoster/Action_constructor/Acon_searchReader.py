
class Acon_SearchReader:
    def setSearch(self):
        sql = "SELECT t_readerbasicinfo.readerId,readerName,readerSex,readerPhone,readerCreditScore from t_readerbasicinfo,t_readerconnection"
        sql += " where t_readerbasicinfo.readerId = t_readerconnection.readerId"
        return sql