from tkinter import *
root = Tk()
root.geometry('500x500')

root.title("Registration Form")

label_0 = Label(root, text="Registration Form", width=20,font=("bold",20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
 
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
