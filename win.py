from tkinter import *
from tkinter import messagebox as mb
from random import sample
import random
from tkinter import messagebox
import datetime
from datetime import *

window2 = Tk()
window2.title("LOTTO")
window2.geometry("700x350")
window2.configure(bg='red')


# Date/Time
now = datetime.now()
add_date = now.strftime("%d / %B/ %Y")
today_date = now.strftime("%H: %M: %P")
datetime = add_date+"\n"+today_date
lbd = Label(window2, text="")
lbd["text"] = datetime
lbd.place(x=400, y=40)

lage_ent = Entry(window2)
lage_ent.place(x=180, y=300)


number1 = IntVar()
number2 = IntVar()
number3 = IntVar()
number4 = IntVar()
number5 = IntVar()
number6 = IntVar()


text1 = Entry(window2, textvariable=number1, font=("bold", 30), width=2)
text1.place(x=10, y=30)
# text1.grid(row=3, column=2)
text2 = Entry(window2, textvariable=number2, font=("bold", 30), width=2)
text2.place(x=70, y=30)
text3 = Entry(window2, textvariable=number3, font=("bold", 30), width=2)
text3.place(x=130, y=30)
text4 = Entry(window2, textvariable=number4, font=("bold", 30), width=2)
text4.place(x=190, y=30)
text5 = Entry(window2, textvariable=number5, font=("bold", 30), width=2)
text5.place(x=250, y=30)
text6 = Entry(window2, textvariable=number6, font=("bold", 30), width=2)
text6.place(x=310, y=30)

result_answer = Label(window2, width=50, height=10)
result_answer.grid(row=12, column=0)
result_answer.place(x=10, y=150)


def play():
    n1 = number1.get()
    n2 = number2.get()
    n3 = number3.get()
    n4 = number4.get()
    n5 = number5.get()
    n6 = number6.get()

    rand_list = [n1, n2, n3, n4, n5, n6]
    rand_list.sort()

    lottocomp = sorted(random.sample(range(1, 49), 6))

    if any(rand_list) < 0 or any(rand_list) < 50:


        if len(lottocomp) == len(rand_list):
            same = set(lottocomp).intersection(set(rand_list))
            if len(same) == 6:
                result_answer.config(text="Jackpot!!! \n" + " You've won - : R10, 000 000.00 " + "\n Today Lotto Numbers are" + str(lottocomp))
            elif len(same) == 5:
                result_answer.config(text=" You hit 5 numbers " + "\n Congratulations:) " + "Payout - R8, 584.00" + "\n Today Lotto Numbers are" + str(lottocomp))
            elif len(same) == 4:
                result_answer.config(text=" You hit 4 numbers " + "\n Congratulations:) " + "Payout - R2, 384.00" + "\n Today Lotto Numbers are" + str(lottocomp))
            elif len(same) == 3:
                result_answer.config(text=" You hit 3 numbers " + "\n Congratulations:) " + "Payout - R100.50" + "\n Today Lotto Numbers are" + str(lottocomp))
            elif len(same) == 2:
                result_answer.config(text=" You hit 2 numbers " + "\n Congratulations:) " + "Payout - R20.00" + "\n Today Lotto Numbers are" + str(lottocomp))
            elif len(same) == 1:
                messagebox.showinfo("RESULT", "You got one number correct :(,  lotto numbers are: " + str(lottocomp))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again, Today's Lotto Numbers are: " + str(lottocomp))
        winners =  lottocomp
        winners = open("winnings.txt", "a")
        winners.write('')
        for item in lottocomp:
            winners.write(item)

        winners.close()




    else:
        messagebox.showinfo("No!", "Please follow the rules.")
        number1.delete(0, END)
        number2.delete(0, END)
        number3.delete(0, END)
        number4.delete(0, END)
        number5.delete(0, END)
        number6.delete(0, END)


button= Button(window2, text="Generate Numbers", bg="yellow", command=play)
button.grid(row=10, column=0)
button.place(x=120, y=130)


# placements
def verify():
    pass


window2.mainloop()

