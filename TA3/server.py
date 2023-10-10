import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

# Create a empty list named clients to hold the incoming connections
clients = []

print("Server has started...")

while True:
    conn, addr = server.accept()
    
    # Print Client connected
    print("Client connected")
    # Append the conn to clients list
    clients.append(conn)

    conn.send("Thank you for connecting".encode())
    conn.close()