import sys
import socket

def mainRun():
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    bind = ("127.0.0.1", 10000)
    sock.bind(bind)
    print>>sys.stderr, 'starting up on %s port %s' % bind
    print("Start Server ")

    while True:
        print >> sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(4096)

        print >> sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >> sys.stderr, data

        if data:
            sent = sock.sendto(data.upper(), address)
            print >> sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    server.close()

if(__name__=="__main__"):
    mainRun()
