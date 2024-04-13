from tkinter import*
win=Tk()

win.attributes('-fullscreen',True)
win.config(bg="#3289a8")
b1=Button(win,text="Information Tecnolongy",font=("arial",22),fg='white',borderwidth=3,relief="groove",bg="black")
b1.place(x=390,y=320)
b2=Button(win,text=" Computer Engineeing ",font=("arial",22),fg='white',borderwidth=3,relief="groove",bg="black")
b2.place(x=390,y=420)
b3=Button(win,text="Mechanical Engineeing",font=("arial",22),fg='white',borderwidth=3,relief="groove",bg="black")
b3.place(x=390,y=520)
b4=Button(win,text="Exait",command=win.destroy)
b4.place(x=800,y=10)
win.mainloop()