
from tkinter import *
from tkinter import messagebox

ourframe = Tk()
ourframe.geometry("500x500")
ourframe.title("ITHUBA NATIONAL LOTTERY")
ourframe.config(bg="white")
photo = PhotoImage(file="lottery.png")
w= Label(ourframe, image=photo)
w.pack()


#function
def verify():
    user_age=int(myentry1.get())
    if user_age >=18:
        messagebox.showinfo("OK", "Great! You can now proceed")

        ourframe.withdraw()
        import win
        win.verify()

    else:
        messagebox.showinfo("OK", "Only users who are above 18 years are allowed to play")



label1 = Label(ourframe, text="Enter your age")
label1.pack()
myentry1 = Entry(ourframe, textvariable="age",fg="black")
myentry1.pack()

#button
mycheck = Button(ourframe, text="OK", command=verify)
mycheck.pack()
ourframe.mainloop()  #calling the function
