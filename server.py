import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 9999

# Create TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

# List of sockets we monitor
sockets_list = [server_socket]

# socket -> user data
clients = {}


def receive_message(client_socket):
    try:
        header = client_socket.recv(HEADER_LENGTH)

        if not len(header):
            return None

        message_length = int(header.decode("utf-8").strip())
        data = client_socket.recv(message_length)

        return header, data

    except:
        return None


while True:

    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list
    )

    for notified_socket in read_sockets:

        # NEW CONNECTION
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is None:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user

            print(f"New user: {user[1].decode('utf-8')}")

        # MESSAGE FROM CLIENT
        else:
            message = receive_message(notified_socket)

            if message is None:
                print(f"Closed connection")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            username = user[1].decode("utf-8")
            msg = message[1].decode("utf-8")

            print(f"{username} > {msg}")

            # broadcast
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user[0] + user[1] + message[0] + message[1])

    for sock in exception_sockets:
        sockets_list.remove(sock)
        del clients[sock]