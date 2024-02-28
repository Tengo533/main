import tkinter as tk

class Calculator():
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x500")
        self.root.title("Calculator")

        self.label = tk.Label(self.root, text="Hello world!", font=('Arial', 18))
        self.label.pack(padx="20", pady="20")

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        # Numbers 1-9

        self.btn1 = tk.Button(self.buttonframe, text="1", font=('Arial', 18))
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="2", font=('Arial', 18))
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="3", font=('Arial', 18))
        self.btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.buttonframe, text="4", font=('Arial', 18))
        self.btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.buttonframe, text="5", font=('Arial', 18))
        self.btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.buttonframe, text="6", font=('Arial', 18))
        self.btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

        self.btn7 = tk.Button(self.buttonframe, text="7", font=('Arial', 18))
        self.btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.buttonframe, text="8", font=('Arial', 18))
        self.btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.buttonframe, text="9", font=('Arial', 18))
        self.btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.btn0 = tk.Button(self.buttonframe, text="0", font=('Arial', 18))
        self.btn0.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.buttonframe.pack(fill='x')

        self.root.mainloop()
Calculator()


