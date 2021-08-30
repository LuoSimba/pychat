
import socket


def CreateServer():
    so = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM)

    so.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            True)

    so.bind(('',9999))
    so.listen(5)
    return so

def HttpProc(server):
    print('=== HTTP PROC ===')
    # socket, str, number
    client, (ip, port) = server.accept()
    print(" * address = %s:%d" % (
        ip,
        port
        ))

    # <class bytes>
    print(' * RECV')
    req = client.recv(4096)
    print(' * RECV ok')
    print(req)
    print(' * RECV end')

    resp = MakeResponse(req)
    client.send(resp)
    client.close()

def MakeResponse(req):

    content = 'hello java world';

    payload = content.encode('utf8')

    parts = [
            b'HTTP/1.0 200 OK',
            b'Content-Length: %d' % len(payload),
            b'',
            payload
            ]
    return b'\r\n'.join(parts)

# -------------------------------
so = CreateServer()

while True:
    HttpProc(so)

so.close()
# -------------------------------
