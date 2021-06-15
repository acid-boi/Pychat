import socket
import threading


a = '''


 ____         ____ _           _   
|  _ \ _   _ / ___| |__   __ _| |_ 
| |_) | | | | |   | '_ \ / _` | __|
|  __/| |_| | |___| | | | (_| | |_ 
|_|    \__, |\____|_| |_|\__,_|\__|
       |___/                       



'''


print(a)
print("Welcome to the PyChat Client application") 
# Choosing the ip and the port of the remote host.

host = input("Please enter the ip address of the remote host: ")
port = int(input("Please enter the port of the remote host to connect on: "))

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break



# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
