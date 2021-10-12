import socket


class ChatClient:

    def __init__(self):
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect(('localhost', 9999))
        self.so = so

    def send(self, msg):
        print("SEND: ", msg)
        sent = self.so.send( msg.encode('utf8') )
        if sent == 0:
            raise RuntimeError()
        print("SEND success")

    def recv(self):
        txt = self.so.recv(4096)
        if txt == b'':
            raise RuntimeError()
        return txt.decode('utf8')

    def quit(self):
        self.so.close()
        print("Client Close")


def main():
    inst = ChatClient()
    inst.send('hello java world')
    txt = inst.recv()
    print('RECV:', txt)
    inst.quit()

if __name__ == '__main__':
    main()

