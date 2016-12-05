import socket

def mainRun():
    server = socket.socket()
    bind = ("127.0.0.1", 5000)
    server.connect(bind)
    data=(raw_input("input Message : "))

    while(data!='q'):
        server.send(data.encode('utf-8'))
        data=server.recv(1024).decode('utf-8')
        print("response from server : "+data)
        data = (raw_input("input Message : "))
    server.close()
if(__name__=="__main__"):
    mainRun()