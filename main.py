from tkinter import*
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
from time import strftime
import mysql.connector
####################################################################################################################################################################3
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="itinfra"
)
###########################################################################################################################################################3

win =Toplevel()
win.attributes('-fullscreen', True)
win.title("MAIN FORM")
win.config(bg="#89CFF0")
l1 = Label(win, text="Institute IT infra Management System", font=("Berlin sans Fb", 30), height=2,width=82,fg='White',bg='black')
l1.place(x=0, y=120)
path = Image.open("logo.png")
render1 = ImageTk.PhotoImage(path)
img = Label(win, image=render1, bg="#89CFF0")
img.place(x=530, y=0)

####################################################################################################################################################

def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, time)
label = Label(win, font=("Imprint MT Shadow", 20), bg="#89CFF0", fg="black")
label.place(x=5, y=5)
t2 = Label(win, text=datetime.date.today(), fg='Black', bg='#89CFF0', font=("Imprint MT Shadow", 25))
t2.place(x=5, y=40)
b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
b4.place(x=1400, y=5)
b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
b5.place(x=1480, y=5)
########################################################################################################################################################################
def clearfield():
    t2.delete(1.0, END)
def user(self):

    def accno(self):
        t2.delete(1.0,END)
        def send():
            s1 = c1.get()
            s2 = c2.get()
            s3 = c3.get()
            s4 = t1.get()
            s5 = t2.get(1.0,END)
            s6 = t3.get(1.0,END)

            print(s1, s2, s3, s4, s5,s6)
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="itinfra"

            )
            mycur = mydb.cursor()
            a = ("insert into  issue(depname,name,selectpc,prodname,asspc,writeprom)values(%s,%s,%s,%s,%s,%s)")
            mycur.execute(a, (s1, s2, s3, s4, s5, s6))
            mydb.commit()
            messagebox.showinfo("CONFIRM", "Record is saved..!")
            clearfield()

        b2 = Button(win, text="     SEND    ", font=("arial", 20, "bold"), relief=RIDGE, borderwidth=5, fg='white', bg='black',command=send)
        b2.place(x=600, y=650)

        clearfield()
        name = str(c2.get())
        name = name[1:][:-1]
        # name=name[0]
        print(name)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="itinfra"

        )
        mycur = mydb.cursor()
        mycur.execute(f"select asspc from facinfo  where name='{name}'")
        data = mycur.fetchone()
        text=""+str(data[0])
        t2.insert(1.0,text)

        # mycur = mydb.cursor()
        # mycur.execute(f"select asspen from facinfo  where name='{name}'")
        # data1 = mycur.fetchone()
        # text1 = " " + str(data1[0])
        # t4.insert(END, text1)

        fac=str(c2.get())
        mycur = mydb.cursor()
        mycur.execute("select depname from facinfo where name='%s'"%(fac))
    depnam = c1.get()
    falculty = ("None")
    if depnam == "Information Technology ":
        mycur = mydb.cursor()
        mycur.execute("select name from facinfo;")
        falculty = mycur.fetchall()
    l2 = Label(win, text="Faculty Name",font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#89CFF0")
    l2.place(x=170, y=350)
    c2 = Combobox(win, values=falculty, font=("arial", 18))
    c2.place(x=420, y=350)
    c2.bind("<<ComboboxSelected>>",accno)
#####################################################################################################################################################################

l3 = Label(win, text="Select Department Name", bd=2, font=("arial", 25), fg='black', borderwidth=0, relief="solid",bg="#89CFF0")
l3.place(x=50, y=250)
dept = ("Information Technology ","Computer Department","Mechanical Engineeing","Electrical Engineeing","Civil Engineeing")
c1 = Combobox(win,values=dept, font=("arial", 18))
c1.place(x=420, y=250)
c1.bind("<<ComboboxSelected>>",user)

#####################################################################################################################################################

l4=Label(win,text="Product Name",font=("Berlin sans Fb",25),fg='black',bg="#89CFF0")
l4.place(x=170,y=450)
t1=Entry(win,bd=2,font=("arial",15))
t1.place(x=420,y=450)
##############################################################################################################################################
l5=Label(win,text="Allocated PC NO",font=("Berlin sans Fb",25),fg='black',bg="#89CFF0")
l5.place(x=750,y=250)
t2=Text(win,bd=2,height=10,width=30,font=("arial",15))
t2.place(x=1050,y=250)
# l5=Label(win,text="Allocated Digital Pen",font=("Berlin sans Fb",25),fg='black',bg="#89CFF0")
# l5.place(x=750,y=350)
# t4=Text(win,bd=2,height=10,width=30,font=("arial",15))
# t4.place(x=1050,y=350)
#####################################################################################################################################################
l6= Label(win, text="Select Problem", font=("Berlin sans Fb", 25), fg='black', bg="#89CFF0")
l6.place(x=170, y=550)
promble= ("AC Problem","Fan Problem","Lab PC Promblem","Window Peomblem","Chair Promblem","Smart Board Promblem","Sound System Promblem")
c3= Combobox(win, values=promble, font=("arial", 15))
c3.place(x=420, y=550)
c3.bind("<<ComboboxSelected>>", )
####################################################################################################################################################
l7= Label(win, text="  Write  Problem  ", font=("Berlin sans Fb", 25), fg='black', bg="#89CFF0")
l7.place(x=750, y=500)
t3= Text(win,height=10,width=30,font=("arial",15))
t3.place(x=1050, y=500)
time()
win.mainloop()
#####################################################################################################################################################################################