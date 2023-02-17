from tkinter import *
root = Tk()
root.configure(bg="coral")
root.geometry("350x230+450+150")
root.title("Base Convertor")


def onClick():
    deci = my_entry.get()
    bina = my_entry.get()
    bina = bin(int(bina)).replace("0b", "")
    octa = my_entry.get()
    octa = oct(int(octa)).replace("0o", "")
    hexa = my_entry.get()
    hexa = hex(int(hexa)).replace("0x", "")

    bina_text = str(bina)
    octa_text = str(octa)
    hexa_text = str(hexa)

    my_label1 = Label(root, text=deci, bg="coral")
    my_label1.grid(row=2, column=1)
    my_label2 = Label(root, text=bina_text, bg="coral")
    my_label2.grid(row=3, column=1)
    my_label3 = Label(root, text=octa_text, bg="coral")
    my_label3.grid(row=4, column=1)
    my_label4 = Label(root, text=hexa_text, bg="coral")
    my_label4.grid(row=5, column=1)
    my_entry.delete(0, END)


my_label = Label(text="Enter a number: ", fg="Blue")
my_label.grid(row=0, column=0, padx=2, pady=2)
my_entry = Entry(root, width=15)
my_entry.grid(row=0, column=1)

sp = Label(text="", bg="coral")
sp.grid(row=1, column=0)

my_label1 = Label(root, text="Decimal:", bg="orange", fg="white")
my_label1.grid(row=2, column=0, sticky='w')
my_label2 = Label(root, text="Binary:", bg="salmon", fg="white")
my_label2.grid(row=3, column=0, sticky='w')
my_label3 = Label(root, text="Octal:", bg="orange", fg="white")
my_label3.grid(row=4, column=0, sticky='w')
my_label4 = Label(root, text="Hexadecimal:", bg="salmon", fg="white")
my_label4.grid(row=5, column=0, sticky='w')

my_button = Button(root, text="Run", command=onClick,
                   width=5, bg="yellow", fg="black")
my_button.grid(row=5, column=3)

my_thanks = Label(root, text="made by-\nManu",
                  bg="black", fg="yellow")
my_thanks.grid(row=6, column=4, padx=55, pady=57)

root.mainloop()
