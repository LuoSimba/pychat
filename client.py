

import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

so.connect(("localhost", 80))

sent = so.send(b'hello java world')

if send == 0:
    raise RuntimeError()

txt = so.recv(4096)
if txt == b'':
    raise RuntimeError()

print(txt.decode('utf8'))

so.close()


