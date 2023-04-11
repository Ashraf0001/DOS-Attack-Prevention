import socket

# Define the maximum number of connections
MAX_CONNECTIONS = 10

# Define the maximum number of requests per connection
MAX_REQUESTS = 100

# Define the maximum request size in bytes
MAX_REQUEST_SIZE = 1024

# Define the port number to listen on
PORT = 8080

# Create a socket object and bind it to a port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))

# Listen for incoming connections
server_socket.listen(MAX_CONNECTIONS)

print(f'Server listening on port {PORT}')

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')
    
    # Set a counter for the number of requests processed
    request_count = 0
    
    while request_count < MAX_REQUESTS:
        # Receive the request data from the client
        request_data = client_socket.recv(MAX_REQUEST_SIZE)
        
        if not request_data:
            # If there is no request data, the client has disconnected
            print(f'Client {client_address} has disconnected')
            break
        
        # Process the request data
        # In this example, we will simply send a response to the client
        response_data = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello, world!</h1>'
        
        # Send the response data to the client
        client_socket.sendall(response_data)
        
        # Increment the request counter
        request_count += 1
        
    # Close the client socket
    client_socket.close()
