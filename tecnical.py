from tkinter import*
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
# mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="itinfra"
#     )
win=Tk()
win.attributes('-fullscreen',True)
win.config(bg='#24ffff')
l1=Label(win,text="  Tecnical Issue  ",font=("arial",25),fg='black',height=2,width=82,borderwidth=3,relief="solid")
l1.place(x=0,y=200)
b1=Button(text="Exit",command=win.destroy)
b1.place(x=50,y=5)
mainloop()