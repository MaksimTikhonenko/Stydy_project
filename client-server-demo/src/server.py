import socket

# https://docs.python.org/3/library/socket.html

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(3)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            print(f"Received: {data.decode('utf-8')}")
            
            reply = f"received {len(data.decode('utf-8'))} characters."
            client_socket.sendall(reply.encode('utf-8'))
        client_socket.close()
        print(f"Connection from {addr} closed")

if __name__ == "__main__":
    start_server()
