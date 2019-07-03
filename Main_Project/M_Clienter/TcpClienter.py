from socket import *
import time


class TcpClienter():
    def send(self,searchData,host = '10.240.253.148'):
        buf = 1024
        addr = (host, 4700)
        cs = socket(AF_INET, SOCK_STREAM, 0)
        cs.connect(addr)
        data = cs.recv(buf).decode('utf-8')
        if data:
            print(data)
            for i in searchData:
                cs.sendall(bytes(i, 'utf-8'))
                time.sleep(0.1)
        time.sleep(0.1)
        cs.sendall(bytes('==','utf-8'))
        emptyList = []
        data = cs.recv(buf).decode('utf-8')
        while data != '==':
            emptyList.append(data.split(','))
            data = cs.recv(buf).decode('utf-8')
        cs.close()
        return emptyList


#searchData = ['陈立达牛逼', '10', '100', '201906', '陈立达', '青州街男子职业技术学院', '0', '0', '==']
#host = '192.168.43.125'
#list = SendToServ.send(searchData,host)
#print(list)
