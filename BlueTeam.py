import socket

def start_client_cxn():
    HOST = "127.0.0.1"
    PORT = 5000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST,PORT))
    message = client_socket.recv(1024)
    print(message.decode())

if __name__ == "__main__":
    start_client_cxn()