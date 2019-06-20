from socket import *
import time
buf = 1024
addr=('192.168.43.125', 4700)
cs=socket(AF_INET,SOCK_STREAM,0)
cs.connect(addr)
data=cs.recv(buf).decode('utf-8')
if data:
    print(data)

    data = ['a', '0', '0', '0', '0', 'None', 'None', 'None']

    for str in data:
        cs.sendall(bytes(str, 'utf-8'))
        time.sleep(0.1)
    cs.sendall(bytes('==', 'utf-8'))
    recKeyWords = []
    while True:
        data = cs.recv(buf).decode('utf-8')
        if data == '==':
            break

        recKeyWords.append(data)
    print(recKeyWords)
cs.close()

