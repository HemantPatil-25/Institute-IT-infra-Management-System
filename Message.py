from tkinter import*
from tkinter.ttk import Combobox
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime
from time import strftime
#######################################################################################################################################################3
def messa():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="itinfra"
        )
    ############################################################################################################################################################
    win=Toplevel()
    win.attributes('-fullscreen',True)
    win.config(bg='#24ffff')
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win, image=render, bg='#24ffff')
    img1.place(x=530, y=0)
    ##############################################################################################################################################################

    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)
    label = Label(win, font=("Imprint MT Shadow", 20), bg="#24ffff", fg="black")
    label.place(x=5, y=5)
    ##########################################################################################################################################################
    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="#24ffff", font=("Imprint MT Shadow", 25))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)


    ##########################################################################"     Function   "#########################################################################################
    def clearfiled():
        c1.delete(0,END)
        t1.delete(1.0,END)
    def solve():
        a = c1.get()
        res = messagebox.askyesno("CONFIRM", "Are you sure..?")
        if res == True:
            mycur = mydb.cursor()
            mycur.execute(f"delete from issue where writeprom='{a}'")
            mydb.commit()
            messagebox.showinfo("CONFIRM", "Record is deleted..!")
            clearfiled()

    ###########################################################################"    Function    "##############################################################################################

    def show(self):
        t1.delete(1.0,END)
        a=c1.get()
        mycur = mydb.cursor()
        mycur.execute(f"select * from issue where writeprom='{a}'",)
        data = mycur.fetchall()
        data=data[0]
        print(data)
        da = "\n\n Faculty Name         : \t" + str(data[0])
        da=da+"\n\n Allocated PC NO     : \t" + str(data[1])
        da=da+"\n\n System Problem      :\t" + str(data[2])
        da=da+"\n\n System Name         :\t" + str(data[3])
        da=da+"\n\n System Issue          :\t" + str(data[4])
        da=da+"\n Deparment Name     :\t" + str(data[5])
        #da=da+"\n Allocated Digital Pen :\t" + str(data[6])

        t1.insert(END, da)

    mycur = mydb.cursor()
    mycur.execute("select writeprom from issue")
    issuename=mycur.fetchall()
    print(issuename)
    arr=[]
    for i in issuename:
        arr.append(i[0])

    ##############################################################################"    Combobox     "############################################################################################

    c1 = Combobox(win, values=arr, state="readonly", font=("arial", 22))
    c1.place(x=500, y=400)
    c1.bind("<<ComboboxSelected>>", show)

    ###############################################################################"       Label   "##########################################################################################

    l1 = Label(win, text=" Show Issue ", relief="solid", bd=2, font=("arial", 25), fg='black', borderwidth=0,bg='#24ffff')
    l1.place(x=300, y=400)
    l2=Label(win,text="        Staff Issue",font=("arial",30),fg='Black',borderwidth=3,relief="solid",height=2,width=80,bg="#A9A9A9")
    l2.place(x=0,y=150)
    l3=Label(win,text=" Problem Statement ",font=("aria l",25),fg='Black',borderwidth=2,relief="solid")
    l3.place(x=1020,y=280)

    ################################################################################"     Text       "###################################################################################

    t1= Text(win,height=15,width=50,font=("arial",15))
    t1.place(x=900, y=350)

    ###############################################################################"     Button     "##################################################################################################################

    b1 = Button(win, text="Issue Solve", font=("arial", 20, "bold"), relief=RIDGE, borderwidth=5, fg='white',bg="black",command=solve)
    b1.place(x=470, y=550)
    time()
    mainloop()
messa()

    #################################################################################################################################################################################
