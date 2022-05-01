
from tkinter import *
root=Tk()
root.title("Chatting Group by AK.")
root.geometry("700x700")

def chatPage(name_value):
    global name
    name=name_value.get()
    print(name)
    root.destroy()

head=Label(root,text='--Welcome Chatting Group--',font=("",35,"bold")).place(relx=0.5, rely=0.1, anchor=CENTER)
f2=Frame(root,bg="grey",padx=50,pady=50)
f2.pack(pady=200)

name_label=Label(f2,text="Name:",font=("",20),padx=10,pady=10,bg="grey")
name_label.grid(row=0,column=0)
name_value=StringVar()

name_entry=Entry(f2,textvariable=name_value,font=("",20))
name_entry.grid(row=0,column=1)

submit_button=Button(f2,text="SUBMIT",font=("",20),command=lambda:chatPage(name_value))
submit_button.grid(row=3,column=1)

root.mainloop()