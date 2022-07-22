from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("Drivers License")

label1=Label(root,text="Driving License")
label1.place(relx=0.5, rely=0.1,anchor=CENTER)

label2=Label(root,text="ID:16567843665478")
label2.place(relx=0.1, rely=0.3,anchor=CENTER)

label3=Label(root,text="Date of Birth: March, 2, 2010")
label3.place(relx=0.1, rely=0.4,anchor=CENTER)

label4=Label(root,text="Pin #: 345678")
label4.place(relx=0.1, rely=0.5,anchor=CENTER)

label5=Label(root,text="Address: Disney Land")
label5.place(relx=0.1, rely=0.6,anchor=CENTER)

label6=Label(root,text="Authorisation: 4")
label6.place(relx=0.1, rely=0.7,anchor=CENTER)