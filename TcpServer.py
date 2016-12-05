import socket

def mainRun():
    server= socket.socket()
    bind = ("127.0.0.1", 5000)
    server.bind(bind)
    server.listen(1)# limit client
    print("wait connect from client ....")
    client,addr = server.accept()
    print ("Connect from : "+str(addr))

    #Process be tween h2h
    while True:
        #input from Client
        data=client.recv(1024).decode('utf-8')
        if(not data):
            break
        print ("Message From Client : "+data)

        data = str(data.upper())
        client.send(data.encode('utf-8'))
    client.close()

if(__name__=="__main__"):
    mainRun()