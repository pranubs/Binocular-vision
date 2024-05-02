import socket

# Define the IP address and port to listen on
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Choose any available port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server listening on port", PORT)
    
    # Accept a connection
    connection, address = server_socket.accept()
    print("Connected to:", address)
    
    # Receive data from the client
    data = connection.recv(1024).decode()
    print("Received:", data)
