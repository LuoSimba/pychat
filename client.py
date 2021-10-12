import socket
import tkinter as tk


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

def main_old():
    so = CreateClient()
    SendMessage(so, 'hello java world')
    txt = RecvMessage(so)
    print(txt)
    so.close()


def UI_CreateWindow():
    def OnBtnUp(event):
        main_old()
    app = tk.Tk()
    app['width']  = 400
    app['height'] = 300
    app.bind('<ButtonRelease-1>', OnBtnUp)
    return app


# Entry 
def main():
    app = UI_CreateWindow()
    print('Click on Window to send message ...')
    print('-----------------------------------')
    app.mainloop()
    print('-----------------------------------')
    print('End')



if __name__ == '__main__':
    main()

