from tkinter import*
from tkinter.ttk import Combobox
import mysql.connector
from PIL import Image,ImageTk
from time import strftime
import datetime
########################################################################################################################################################
def show():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="itinfra"

    )
    ###########################################################################################################################################################
    win=Toplevel()
    win.attributes('-fullscreen',True)
    win.config(bg="#20B2AA")
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win, image=render,bg="#20B2AA")
    img1.place(x=550, y=0)
    ###############################################################################################################################################

    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)


    label = Label(win, font=("Imprint MT Shadow", 20), bg="#20B2AA", fg="black")
    label.place(x=5, y=5)

    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="#20B2AA", font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)

    def clearfield():
        t1.delete(0, END)
    def dep(self):
        def accno(self):
            clearfield()
            name = str(c2.get())
            name = name[1:][:-1]
            print(name)
            mycur = mydb.cursor()
            mycur.execute(f"select asspc from facinfo  where name='{name}'")
            data = mycur.fetchone()
            t1.insert(0,data)
            fac=str(c2.get())
            mycur = mydb.cursor()
            mycur.execute("select depname from facinfo where name='%s'"%(fac))
            print(depnam,name,data[0])

            da = "\n All Reocrd"
            da = da + "\n\nSelect Department Name   :" + str(depnam)
            da = da + "\nFaculty Name                 :" + str(name)
            da = da + "\nAllow PC No                   :" + str(data[0])
            t2.insert(1.0, da)
        depnam = c1.get()
        falculty = ("None")
        if depnam == "Information Technology ":
            mycur = mydb.cursor()
            mycur.execute("select name from facinfo;")
            falculty = mycur.fetchall()

    ##########################################################################################################################################

        l2 = Label(win, text="Faculty Name",font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#20B2AA")
        l2.place(x=220, y=450)
        c2 = Combobox(win, values=falculty, font=("arial", 22))
        c2.place(x=470, y=450)

        c2.bind("<<ComboboxSelected>>",accno)
    ##########################################################################################################################################################

    l3 = Label(win, text="Select Department Name", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#20B2AA")
    l3.place(x=50, y=350)
    dept = ("Information Technology ","Computer Department","Mechanical Engineeing","Electrical Engineeing","Civil Engineeing")
    c1 = Combobox(win,values=dept, font=("arial", 22))
    c1.place(x=470, y=350)
    c1.bind("<<ComboboxSelected>>", dep)

    ######################################################################################################################################################

    l4=Label(win,text="Show Record",font=("arial",30),fg='Black',borderwidth=3,relief="solid",height=2,width=80,bg="#A9A9A9")
    l4.place(x=0,y=180)
    l1= Label(win, text="Allow PC No", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#20B2AA")
    l1.place(x=220, y=550)
    t1=Entry(win,bd=2,font=("arial",22))
    t1.place(x=470,y=550)
    t2= Text(win,height=15,width=50,font=("arial",15))
    t2.place(x=900, y=300)

    time()
    mainloop()
show()

    ######################################################################################################################################

