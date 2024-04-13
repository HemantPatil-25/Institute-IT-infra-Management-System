from tkinter import*
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
from time import strftime
import mysql.connector
import datetime
########################################################################################################################################################################
def delet():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="itinfra"

    )
    ###############################################################################################################################################################
    win=Toplevel()
    win.attributes('-fullscreen',True)
    win.config(bg="#7393B3")
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win,image=render,bg="#7393B3")
    img1.place(x=530,y=0)

    #########################################################################################################################################################
    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)

    ####################################################################################################################################################
    label = Label(win, font=("Imprint MT Shadow", 20), bg="#7393B3", fg="black")
    label.place(x=5, y=5)
    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="#7393B3", font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)
    #############################################################################################################################################33
    def clearfield():
        t1.delete(0, END)
        t3.delete(0,END)

    def dep(self):

        def accno(self):
            t1.delete(0,END)
            t3.delete(0,END)
            #clearfield()
            name = str(c2.get())
            name = name[1:][:-1]
            # name=name[0]
            print(name)
            mycur = mydb.cursor()
            mycur.execute(f"select asspc from facinfo  where name='{name}'")
            data = mycur.fetchall()
            t1.insert(0, data)

            mycur = mydb.cursor()
            mycur.execute(f"select asspen from facinfo  where name='{name}'")
            data1= mycur.fetchall()
            t3.insert(0, data1)

            fac=str(c2.get())
            mycur = mydb.cursor()
            mycur.execute("select depname from facinfo where name='%s'"%(fac))
        depnam = c1.get()
        falculty = ("None")
        if depnam == "Information Technology ":
            mycur = mydb.cursor()
            mycur.execute("select name from facinfo;")
            falculty = mycur.fetchall()
        l2 = Label(win, text="Faculty Name",font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#7393B3")
        l2.place(x=600, y=360)
        c2 = Combobox(win, values=falculty, font=("arial", 22))
        c2.place(x=850, y=360)
        c2.bind("<<ComboboxSelected>>",accno)
    ########################################################################################################################################################
    l3 = Label(win, text="Select Department Name", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#7393B3")
    l3.place(x=450, y=300)

    dept = ("Information Technology ","Computer Department","Mechanical Engineeing","Electrical Engineeing","Civil Engineeing")
    c1 = Combobox(win,values=dept, font=("arial", 22))
    c1.place(x=850, y=300)
    c1.bind("<<ComboboxSelected>>", dep)

    #####################################################################################################################################################
    def delrec():
        s1 = t1.get()
        s2 = t3.get()
        res = messagebox.askyesno("CONFIRM", "Are you sure..?")
        #print(res)

        if res == True:
            mycur = mydb.cursor()
            mycur.execute("delete from facinfo where asspc=" + str(s1,s2))
            mydb.commit()
            messagebox.showinfo("CONFIRM", "Record is deleted..!")
            t1.delete(0, END)
            t3.delete(0,END)
            clearfield()
        else:
            pass


    ############################################################################################################################################################
    l3=Label(win,text="Delete Record",font=("arial",30),fg='Black',borderwidth=3,relief="solid",height=2,width=80,bg="#A9A9A9")
    l3.place(x=0,y=150)
    #######################################################################################################################################################
    l1= Label(win, text="Allow PC No", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#7393B3")
    l1.place(x=600, y=450)
    t1=Entry(win,bd=2,font=("arial",22))
    t1.place(x=850,y=450)

    l2= Label(win, text="Allow digital Pen", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#7393B3")
    l2.place(x=600, y=520)
    t3=Entry(win,bd=2,font=("arial",22))
    t3.place(x=850,y=520)

    b2 = Button(win, text="Delete RECORD", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=5, fg='white',bg="black",command=delrec)
    b2.place(x=800, y=580)

    time()
    mainloop()
delet()
    ###############################################################################################################################################################
