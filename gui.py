from tkinter import *
from tkinter import messagebox
insertText = "print"

def get_whiteDisks():
    whiteDisks = float(ENTRY2.get())
    return whiteDisks
def get_blackDisks():
    blackDisks = float(ENTRY1.get())
    return blackDisks
    
def start():
    print("started")
    return None
    

def reset():
    ENTRY1.delete(0, END)
    ENTRY1.insert(END, 0)

    ENTRY2.delete(0, END)
    ENTRY2.insert(END, 0)
    print("Reseting")

if __name__ == '__main__':
    TOP = Tk()
    TOP.geometry("400x400")
    TOP.configure(background="#8c52ff")
    TOP.title("Order collecter")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#8c52ff",fg="#ffffff", text="Please fill in your order: ", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=80, y=0)
    LABLE1 = Label(TOP, bg="#ffffff", text="Black Disks: ", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#ffffff", text="White Disks: ", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)

    LABLE3 = Label(TOP, bg="#8c52ff", text=insertText, bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE3.place(x=55, y=190)

    ENTRY2 = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON1 = Button(bg="#000000",fg='#ffffff', bd=12, text="Start", padx=20, pady=10, command= start,
                    font=("Helvetica", 10, "bold"))
    BUTTON1.grid(row=5, column=0, sticky=W)

    BUTTON1.place(x=100, y=250)

    BUTTON2 = Button(bg="#000000",fg='#ffffff', bd=12, text="Reset", padx=20, pady=10, command=reset,
                    font=("Helvetica", 10, "bold"))
    BUTTON2.grid(row=5, column=0, sticky=W)
    BUTTON2.place(x=200, y=250)
    TOP.mainloop()