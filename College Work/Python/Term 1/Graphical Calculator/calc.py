import tkinter as tk
from tkinter import *
main = tk.Tk()
main.geometry("500x500")
main.title("Calculator")

display_input = StringVar()

display = Entry(main, textvariable=display_input)

display.grid(columnspan=4)

button1 = Button(main, text="1", fg="black", bg="red")
button1.grid(row=2, column=0)

button1 = Button(main, text="2", fg="black", bg="red")
button1.grid(row=2, column=1)

button1 = Button(main, text="3", fg="black", bg="red")
button1.grid(row=2, column=2)

button1 = Button(main, text="4", fg="black", bg="red")
button1.grid(row=1, column=0)

button1 = Button(main, text="5", fg="black", bg="red")
button1.grid(row=1, column=1)

button1 = Button(main, text="6", fg="black", bg="red")
button1.grid(row=1, column=2)

button1 = Button(main, text="7", fg="black", bg="red")
button1.grid(row=0, column=0)

button1 = Button(main, text="8", fg="black", bg="red")
button1.grid(row=0, column=1)

button1 = Button(main, text="9", fg="black", bg="red")
button1.grid(row=0, column=2)

button1 = Button(main, text="0", fg="black", bg="red")
button1.grid(row=2, column=0)












main.mainloop()