from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Turtle Code")

input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black",
highlightcolor="black", highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'),
textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text = "C", fg="black",
width=32, height=3, bd=0, bg="#eee", cursor="hand2")

clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text = "/", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

divide.grid(row=0, column=3, padx=1, pady=1)

seven = Button(btns_frame, text = "7", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text = "8", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text = "9", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text = "*", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

multiply.grid(row=1, column=3, padx=1, pady=1)

four = Button(btns_frame, text = "4", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

four.grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text = "5", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

five.grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text = "6", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text = "-", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

minus.grid(row=2, column=3, padx=1, pady=1)

one = Button(btns_frame, text = "1", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

one.grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text = "2", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

two.grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text = "3", fg="black",
width=10, height=3, bd=0, bg="#fff", cursor="hand2")

three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text = "+", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

plus.grid(row=3, column=3, padx=1, pady=1)

zero = Button(btns_frame, text = "0", fg="black",
width=21, height=3, bd=0, bg="#fff", cursor="hand2")

zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text = ".", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

point.grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text = "=", fg="black",
width=10, height=3, bd=0, bg="#eee", cursor="hand2")

equals.grid(row=4, column=3, padx=1, pady=1)

win.mainloop()