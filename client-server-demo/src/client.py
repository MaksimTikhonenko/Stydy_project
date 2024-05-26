import socket

# https://docs.python.org/3/library/socket.html

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting.....")
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    try:
        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            if not data:
                break

            print(f"Server says: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Client closing...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
