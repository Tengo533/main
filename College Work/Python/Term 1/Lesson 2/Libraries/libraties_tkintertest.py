from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Enter Meters', borderwidth=2, relief="sunken")
        self.lbl1.place(x=100, y=50)
        self.t1=Entry(bd=3)
        self.t1.place(x=200, y=50)
        self.lbl3=Label(win, text='In Feet', borderwidth=2, relief="sunken")
        self.lbl3.place(x=100, y=150)
        self.t3=Entry()
        self.t3.place(x=200, y=150)
        self.b1=Button(win, text='Convert', command=self.convert, borderwidth=2, relief="solid")
        self.b1.place(x=100, y=100)
    def convert(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        if isinstance(num1, int):
            result=num1 * 3.281
            self.t3.insert(END, str(result))
        else:
            self.t3.insert(END, str("Please input a number"))


window=Tk()
mywin=MyWindow(window)
window.title('Python KG To Ounces Converter')
window.geometry("400x200+10+10")
window.configure(bg='light green')
window.mainloop()
