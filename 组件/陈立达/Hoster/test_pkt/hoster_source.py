from socket import *
from time import ctime
host='192.168.43.125'
port=4700
Buf=1024
addr=(host,port)
s=socket(AF_INET,SOCK_STREAM,0)
s.bind(addr)
s.listen(20)

while True:
    print('等待客户连接...\r\n')
    cs,caddr=s.accept()
    print('...连接来自于:',caddr)
    data='欢迎你的到来！\r\n'
    cs.sendall(bytes(data,'utf-8'))
    data=cs.recv(Buf).decode('utf-8')
    if not data:
        break
    data='[%s]%s\r\n'%(ctime(),data)
    cs.sendall(bytes(data,'utf-8'))
    print(data)
    cs.close()
s.close()