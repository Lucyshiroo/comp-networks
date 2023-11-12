import socket
import sys
import time

def send_request(server_ip, port, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (server_ip, port)

    try:
        client.connect(server_address)

        # Sending a simple GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        start_time = time.time()
        client.send(request.encode())

        # Receiving and printing the server's response
        response = client.recv(4096).decode()
        elapsed_time = time.time() - start_time
        print(f"Response from server:\n{response}")
        print(f"Round Trip Time (RTT): {elapsed_time:.4f} seconds")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_ip> <port> <filename>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    send_request(server_ip, port, filename)
