from M_Hoster.M_Control import MC_SignIn
from V_windows.V_readerEntrance import V_SignIn
from M_Clienter import TcpClienter
class VC_SignIn:
    def ensure(self,userId,pwd):
        list = []
        list.append("10")
        list.append(str(userId))
        list.append(str(pwd))
        list.append("==")
        a = TcpClienter.TcpClienter()
        list = a.send(list)
        V_SignIn.status = int(list[0][0])
        #a = MC_SignIn.MC_SignIn()
        #V_SignIn.status = a.sign(userId,pwd)