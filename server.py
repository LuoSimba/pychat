
import socket
import select


def CreateServer():
    # create an INET, STREAMing socket
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

def Connection(server):
    print('=== Connection ===')
    # socket, str, number
    client, (ip, port) = server.accept()
    print(" * address = %s:%d" % (
        ip,
        port
        ))

    potential_readers.add( client )

def HttpProc(client):
    # <class bytes>
    print(' * RECV')
    # When a recv() returns 0 bytes, it means
    # the other side has closed (or is in the
    # process of closing) the connection.
    req = client.recv(4096)
    print(' * RECV ok')
    print(req)
    print(' * RECV end')

    resp = MakeResponse(req)
    client.send(resp)
    client.close()

    potential_readers.discard( client )


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

potential_readers = set()
potential_writers = set()
potential_errs    = set()

potential_readers.add( so )


while True:
    print('.')

    rs, ws, es = select.select(
            potential_readers,
            potential_writers,
            potential_errs,
            10000
            )

    for s in rs:
        if s is so:
            Connection(s)
        else:
            HttpProc(s)

so.close()
# -------------------------------
