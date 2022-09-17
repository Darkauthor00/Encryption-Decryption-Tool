from cProfile import label
from tkinter import messagebox
from cgitb import reset, text
from email import message
from telnetlib import ENCRYPT
from tkinter import*
import base64
from webbrowser import get

screen = Tk()
screen.geometry("420x420")
screen.title ("encryption&decryption")
screen.configure(bg="grey")
def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("420x250")
        screen1.configure(bg="grey")
        
        message=Text1.get(1.0,END)
        encode_message=message.encode("ascii") 
        base64_byets=base64.b64encode(encode_message) 
        encrypt = base64_byets.decode("ascii")
        
        Label(screen1,text="code is encrypted",font="impack 14 bold").place(x=5,y=6) 
        text2=Text(screen1,font="30",bd="4",wrap="word") 
        text2.place(x=2,y=30,width=390,height=180)  
        text2.insert(END,encrypt)
    elif(password==""):
        messagebox.showerror("ERROR","PLEASE ENTER THE SECRET KEY")
    elif(password!="1234"):
        messagebox.showerror("SORRY","THE SECRET KEY IS INVAILD")
        
def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("420x250")
        screen2.configure(bg="grey")
        
        message=Text1.get(1.0,END)
        encode_message=message.encode("ascii") 
        base64_byets=base64.b64decode(encode_message) 
        encrypt = base64_byets.decode("ascii")
        
        Label(screen2,text="code is decrypted",font="impack 14 bold").place(x=5,y=6) 
        text2=Text(screen2,font="30",bd="4",wrap="word") 
        text2.place(x=2,y=30,width=390,height=180)  
        text2.insert(END,encrypt)
    elif(password==""):
        messagebox.showerror("ERROR","PLEASE ENTER THE SECRET KEY")
    elif(password!="1234"):
        messagebox.showerror("SORRY","THE SECRET KEY IS INVAILD")


def reset():
    Text1.delete(1.0,END)
    code.set("")
                   
        
#label

Label(screen,text="enter the text for encryption & decryption",font="impack 15 bold",bg="white").place(x=7,y=9)

#text
Text1=Text(screen,font="20")
Text1.place(x=5,y=45,width=411,height=120)
#label
Label(screen,text="enter secret key",font="impack 13 bold").place(x=150,y=180)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=120,y=240)
#button
Button(screen,text="ENCRYPT",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=15,y=280)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="green",fg="white",command=decrypt).place(x=160,y=280)
Button(screen,text="RESET",font="arial 15 bold",bg="blue",fg="white",command=reset).place(x=300,y=280)

mainloop()
