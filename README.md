# comp-networks
# Web Server and Client Example

## Author

[Your Name]

## Overview

# Simple Multithreaded Web Server & Client

This project consists of a multithreaded web server and a single-threaded web client implemented in Python. The server listens for incoming HTTP requests and serves files concurrently to multiple clients, while the client initiates connections to the server, sends HTTP GET requests, and displays server responses.

## Server

### How to Run

1. Open a terminal and navigate to the directory containing `server.py`.
2. Run the server using the command:

    ```bash
    python server.py
    ```

3. The server will start listening on `0.0.0.0:8080` by default.

### Server Behavior

- The server responds to HTTP GET requests.
- It looks for requested files in the server's local directory.
- If the requested file is found, it sends a "200 OK" response with the file content.
- If the file is not found, it sends a "404 Not Found" response.
- In case of errors, it sends a "400 Bad Request" response.

## Client

### How to Run

1. Open another terminal and navigate to the directory containing `client.py`.
2. Run the client using the command:

    ```bash
    python client.py 127.0.0.1 8080 index.html
    ```

3. Adjust the server IP, port, and filename as needed.

### Client Behavior

- The client initiates a connection to the server.
- It sends an HTTP GET request for a specific file.
- It measures and displays the Round Trip Time (RTT).
- It displays the server's response.

### Sample Commands

- To request `index.html` from the server:

    ```bash
    python client.py 127.0.0.1 8080 index.html
    ```




