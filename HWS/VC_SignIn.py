import MC_SignIn
import V_SignIn

class C_SignIn:
    def ensure(self,userId,pwd):
        a = MC_SignIn.MC_SignIn()
        V_SignIn.status = a.sign(userId,pwd)