import socket
import threading
import os

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Received request: {request}")

    try:
        # Extracting requested filename from the request
        filename = request.split()[1][1:]
        if not filename:
            filename = "index.html"  # Default file

        with open(filename, 'rb') as file:
            content = file.read()
            response = f"HTTP/1.1 200 OK\r\n\r\n{content.decode('utf-8')}"
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\n\r\n404 Error: File not found"
    except Exception as e:
        response = "HTTP/1.1 400 Bad Request\r\n\r\n400 Error: Bad request"

    client_socket.send(response.encode())
    client_socket.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[*] Listening on 0.0.0.0:{port}")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    port_number = 8080  # You can change this port if needed
    start_server(port_number)
