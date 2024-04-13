from tkinter import*
from tkinter.ttk import Combobox
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime
from time import strftime
###################################################################################################################################################################
def new():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="itinfra"
        )
    ####################################################################################################################################################33
    win=Toplevel()
    win.attributes('-fullscreen',True)
    win.config(bg="#F0E68C")
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win, image=render,bg="#F0E68C")
    img1.place(x=530,y=0)

    ########################################################################################################################################################
    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)
    label = Label(win, font=("Imprint MT Shadow", 20), bg="#F0E68C", fg="black")
    label.place(x=5, y=5)
    ######################################################################################################################################################3
    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="#F0E68C", font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)

    ########################################################################################################################################################################3
    def save():
        s1 = c1.get()
        s2 = t1.get()
        s3 = t2.get()
        s4 = t3.get()
        if s1 == "":
            messagebox.showwarning("WARNING..!", "Please enter Department's name..")
            return
        if s2 == "":
            messagebox.showwarning("WARNING..!", "Please enter Faculty's name..")
            return
        if s3 == "":
            messagebox.showwarning("WARNING..!", "Please enter Allow PC NO address..")
            return
        if s4 == "":
            messagebox.showwarning("WARNING..!", "Please enter Allow Digital Pen address..")
            return

        mycur = mydb.cursor()
        a=("insert into  facinfo(depname,name,asspc,asspen)values(%s,%s,%s,%s)")
        mycur.execute(a,(s1,s2,s3,s4))
        mydb.commit()
        messagebox.showinfo("CONFIRM", "Record is saved..!")
        t1.delete(0, END)
        c1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0,END)
        mycur = mydb.cursor()
    ################################################################################################################################################################################

    l1=Label(win,text=" New Record ",font=("arial",25),fg='black',height=2,width=82,borderwidth=3,relief="solid")
    l1.place(x=0,y=150)
    l1= Label(win, text="Select Department Name", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#F0E68C")
    l1.place(x=450, y=300)
    dept = ("Information Technology ", "Computer Department,","Mechanical Engineeing","Civil Engineeing","Electrical Engineeing")
    c1 = Combobox(win, values=dept, state="readonly", font=("arial", 22))
    c1.place(x=850, y=300)
    c1.bind("<<ComboboxSelected>>", dept)
    ##########################################################################################################################################################
    l1= Label(win, text="New Faculty", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#F0E68C")
    l1.place(x=600, y=400)
    t1=Entry(win,bd=2,font=("arial",22))
    t1.place(x=850,y=400)
    ##########################################################################################################################################################
    l1= Label(win, text="Allow PC No", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#F0E68C")
    l1.place(x=600, y=480)
    t2=Entry(win,bd=2,font=("arial",22))
    t2.place(x=850,y=480)
    ##############################################################################################################################################################
    l1= Label(win, text="Allow digital Pen", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#F0E68C")
    l1.place(x=600, y=560)
    t3=Entry(win,bd=2,font=("arial",22))
    t3.place(x=850,y=560)
    ######################################################################################################################################################
    b2 = Button(win, text="SAVE RECORD", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=5, fg='white', bg='black',command=save)
    b2.place(x=800, y=620)

    time()
    mainloop()
new()

#########################################################################################################################################################