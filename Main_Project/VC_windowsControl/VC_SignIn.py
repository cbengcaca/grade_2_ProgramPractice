from M_Hoster.M_Control import MC_SignIn
from V_windows.V_readerEntrance import V_SignIn
from M_Clienter import TcpClienter
class VC_SignIn:
    def ensure(self,userId,pwd):
        a = MC_SignIn.MC_SignIn()
        V_SignIn.status = a.sign(userId,pwd)