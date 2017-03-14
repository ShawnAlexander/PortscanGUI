import socket

def KnockKnock(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        client.settimeout(0.01)
        client.connect((host, port))
    except OSError as e:
        client.close()
        return False
    client.close()
    return True