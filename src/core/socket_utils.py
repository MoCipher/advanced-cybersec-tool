def create_socket():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def send_data(sock, data, address):
    sock.connect(address)
    sock.sendall(data)
    sock.close()

def receive_data(sock, buffer_size=1024):
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(buffer_size)
    conn.close()
    return data, addr