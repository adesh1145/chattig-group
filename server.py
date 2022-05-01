import socket
from threading import Thread
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost",5501))

server.listen()
global all_client
all_client={}
print("--Server--")
def all_send(client):
    while True:
        try:
            msg=client.recv(1024)
            for i in all_client:
                if i !=client:
                    i.send(msg)
        except:
            for i in all_client:
                if i !=client:
                    i.send(f"{all_client[client]} are Disconnected".encode())
            
            del all_client[client]
            client.close()
            break


while True:

    print("Waiting for Connection......")
    client,addr=server.accept()
    print(client,addr)
    print("Connection are Established.....") 
    
    name=client.recv(1024).decode()
    all_client[client]=name
    for i in all_client:
        if i !=client:
            i.send(f"{name} are connected".encode())

    thread2=Thread(target=all_send,args=(client,))
    thread2.start()


