import socket

def CreateClient():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.connect(("localhost", 9999))
    return so

def SendMessage(conn, msg):
    print("SEND:", msg)
    sent = conn.send( msg.encode('utf8') )
    if sent == 0:
        raise RuntimeError()

def RecvMessage(conn):
    txt = conn.recv(4096)
    if txt == b'':
        raise RuntimeError()
    return txt.decode('utf8')

def main():
    so = CreateClient()
    SendMessage(so, 'hello java world')
    txt = RecvMessage(so)
    print(txt)
    so.close()


if __name__ == '__main__':
    main()

