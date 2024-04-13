from tkinter import*
from PIL import Image,ImageTk
from time import strftime
import datetime

def mainwin():
    win=Tk()
    win.attributes('-fullscreen',cTrue)

###########################################################################################################################################################
    path1 = Image.open("iitt.jpg")
    render1 = ImageTk.PhotoImage(path1)
    img = Label(win, image=render1)
    img.place(x=0, y=0)

    path = Image.open("logo.png")
    render= ImageTk.PhotoImage(path)
    img1= Label(win, image=render,bg='white')
    img1.place(x=530, y=0)
#############################################################################################################################################


    def time():
        string=strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000,time)
    label=Label(win,font=("Imprint MT Shadow",20),bg="white",fg="black")
    label.place(x=5,y=5)

    t2 = Label(win, text=datetime.date.today(), fg='Black', bg='white', font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)


################################################################################################################################################

    def logi():
        import loginadmin
        loginadmin.logi()
    B1=Button(win, text="           Admin Login         ", font=("arial", 30), fg='white', bg='black',borderwidth=8, relief=RIDGE, command=logi)
    B1.place(x=500, y=400)


##############################################################################################################################################

    def userlog():
        import userlogin
        userlogin.userlog()

    B2 =Button(win, text="            User Login          ", font=("arial", 30), fg='white', bg='black',borderwidth=8, relief=RIDGE,command=userlog)
    B2.place(x=500, y=530)

####################################################################################################################################################################


    ##########################################################################################################################################################
    l1 = Label(win, text="  IT INFRA MANAGEMENT SYSTEM  ", font=("arial", 25), fg='white', height=2, width=82,borderwidth=3, relief="solid", bg='black')
    l1.place(x=0, y=200)

######################################################################################################################################

    b4= Button(win, text="Back",bg="green",fg='white',font=("arial", 13,"bold"),relief=RIDGE,borderwidth=5 ,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit",bg="red",fg='white',font=("arial", 13,"bold"),relief=RIDGE,borderwidth=5,command=quit)
    b5.place(x=1480, y=5)
    time()
    mainloop()
mainwin()