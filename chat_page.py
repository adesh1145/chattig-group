import name_page
from tkinter import*
import socket
from threading import Thread

root=Tk()
root.title("Chatting Group by AK.")
root.geometry("700x700")

def send(client):
    # while True:
    try:
        msg=msg_entry.get(1.0, "end-1c")
        client.send(f"{name}:{msg}".encode())
        mylist.insert(END,f"You:{msg}")
        msg_entry.delete(1.0, "end")
    except:
        client.close()
        root.destroy()
        # break


def receive(client):
    while True:
        try:
            msg=client.recv(1024).decode()
            mylist.insert(END,f"{msg}")
            
        except:
            client.close()
            root.destroy()
            break



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name=name_page.name


client.connect(("localhost",5501))
client.send(name.encode())

thread=Thread(target=receive,args=(client,))
thread.start()

scroll=Scrollbar(root)
scroll.place(y=680,height=600)
mylist=Listbox(root,yscrollcommand=scroll.set,font=("",20))
mylist.place(height=600,width=680)
scroll.config(command=mylist.yview)

msg_entry=Text(root,font=("",20))
msg_entry.place(x=0,y=600,height=100,width=600)
send_button=Button(root,text="Send",font=("",20),command=lambda:send(client))
send_button.place(x=600,y=600,height=100,width=100)

root.mainloop()