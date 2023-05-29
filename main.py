import socket

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5000  # Choose the same port number as in the Android code

def handle_client_connection(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Process the received data
        received_data = data.decode('utf-8')
        print('Received data:', received_data + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Add your logic here to handle the received gyrodata

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Set the option to reuse the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to a specific host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print('Waiting for a connection...')

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Connected to:', client_address)

        # Handle the client connection in a separate thread
        handle_client_connection(client_socket)

