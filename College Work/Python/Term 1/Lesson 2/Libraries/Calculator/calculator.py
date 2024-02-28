from tkinter import *

class Calculator:
    def __init__(self, win):

        self.b1=Button(win, text='+', height="5", width="8", comand=self.add()) # + Button
        self.b1.place(x=0, y=200)

        self.b2=Button(win, text='-', height="5", width="8")  # - Button
        self.b2.place(x=70, y=200)

        self.b3=Button(win, text='*', height="5", width="8")  # * Button
        self.b3.place(x=140, y=200)

        self.b4=Button(win, text='/', height="5", width="8")  # / Button
        self.b4.place(x=210, y=200)

        self.b5=Button(win, text='9', height="5", width="8")  # 9 Button
        self.b5.place(x=0, y=290)

        self.b6=Button(win, text='8', height="5", width="8")  # 8 Button
        self.b6.place(x=70, y=290)

        self.b7=Button(win, text='7', height="5", width="8")  # 7 Button
        self.b7.place(x=140, y=290)

        self.b8=Button(win, text="Clear", height="5", width="8")
        self.b8.place(x=210, y=290)

        self.b9=Button(win, text='6', height="5", width="8")  # 6 Button
        self.b9.place(x=0, y=380)

        self.b10=Button(win, text='5', height="5", width="8")  # 5 Button
        self.b10.place(x=70, y=380)

        self.b11=Button(win, text='4', height="5", width="8")  # 4 Button
        self.b11.place(x=140, y=380)

        self.b12=Button(win, text='3', height="5", width="8")  # 3 Button
        self.b12.place(x=0, y=470)
        
        self.b13=Button(win, text='2', height="5", width="8")  # 2 Button
        self.b13.place(x=70, y=470)

        self.b14=Button(win, text='1', height="5", width="8")  # 1 Button
        self.b14.place(x=140, y=470)

        self.b15=Button(win, text='0', height="5", width="8")  # 0 Button
        self.b15.place(x=210, y=470)
        
    def add(self):
        print("test test test")    





window = Tk()
window.title('Calculator')
mywin=Calculator(window)
window.geometry("300x600")
window.configure(bg='gray')
window.mainloop()