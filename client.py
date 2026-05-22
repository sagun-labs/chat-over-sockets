import socket
import select
import sys
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 9999

username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

# Send username
encoded_username = username.encode("utf-8")
username_header = f"{len(encoded_username):<{HEADER_LENGTH}}".encode("utf-8")

client_socket.send(username_header + encoded_username)


while True:

    # SEND MESSAGE
    message = input(f"{username} > ")

    if message:
        encoded_message = message.encode("utf-8")
        message_header = f"{len(encoded_message):<{HEADER_LENGTH}}".encode("utf-8")

        client_socket.send(message_header + encoded_message)

    # RECEIVE MESSAGE
    try:
        while True:

            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header):
                print("Server closed connection")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())

            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno not in (errno.EAGAIN, errno.EWOULDBLOCK):
            print("Read error:", str(e))
            sys.exit()

    except Exception as e:
        print("Error:", str(e))
        sys.exit()