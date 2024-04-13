from tkinter import*
from PIL import Image,ImageTk
import datetime
from time import strftime
from gtts import gTTS
from playsound import playsound
from tkinter import messagebox
#################################################################################################################################################################################################
def admin():
    win = Toplevel()
    win.attributes('-fullscreen', True)
    win.config(bg="#7393B3")
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win, image=render)
    img1.place(x=530, y=0)
############################################################################################################################################################################################3
    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)
    label = Label(win, font=("Imprint MT Shadow", 20), bg="#7393B3", fg="black")
    label.place(x=5, y=5)
    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="#7393B3", font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
########################################################################################################################################################################################################################

    l1 = Label(win, text="  IT INFRA MANAGEMENT SYSTEM  ", font=("arial", 25), fg='black', height=2, width=82,borderwidth=3, relief="solid")
    l1.place(x=0, y=200)
    b4 = Button(win, text="Back", bg="green", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit", bg="red", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)

##############################################################################################################################################################################################################
    def new():
        import newrecord
        newrecord.new()
    b1 = Button(win, text="       New Faculty Record       ", font=("arial", 25), fg='black', borderwidth=3, relief="solid",command=new)
    b1.place(x=300, y=350)
#########################################################################################################################################################################################################

    def delet():
        import DeleteRecord
        DeleteRecord.delet()
    b2 = Button(win, text="       Delete Faculty Record    ", font=("arial", 25), fg='black', borderwidth=3, relief="solid",command=delet)
    b2.place(x=800, y=350)

######################################################################################################################################################################################################################3
    def show():
        import ShowRecord
        ShowRecord.show()

    b5 = Button(win, text="        Show Faculty Record     ", font=("arial", 25), fg='black', borderwidth=3, relief="solid",command=show)
    b5.place(x=300, y=480)

##########################################################################################################################################################################################################3

    def messa():
        import Message
        Message.messa()
    b3 = Button(win, text="       Faculty  Message        ", font=("arial", 25), fg='black', borderwidth=3, relief="solid",command=messa)
    b3.place(x=800, y=480)

#############################################################################################################################################################
    # mytext = 'Welcome to Admin Login!'
    # language = 'en'
    # myobj = gTTS(text=mytext, lang=language, slow=False)
    # myobj.save("welcome.mp3")
    # playsound('welcome.mp3')
    # print('playing sound using playsound')
##########################################################################################################################################
    time()
    win.mainloop()
admin()
####################################################################################################################################################################