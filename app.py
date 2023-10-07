import sympy
from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entrada = Entry(font="Arial 32")
        self.entrada.place_configure(x=50, y=50)

        self.resultado = Label(text="Bem vindo.", font="Arial 30", border=True, borderwidth=2)
        self.resultado.place_configure(x=700, y=50)

        # row 2
        self.b1 = Button(text="1", font="Arial 25", width=3, height=2, command=lambda: self.click("1"))
        self.b1.place_configure(x=50, y=150)

        self.b2 = Button(text="2", font="Arial 25", width=3, height=2, command=lambda: self.click("2"))
        self.b2.place_configure(x=150, y=150)

        self.b3 = Button(text="3", font="Arial 25", width=3, height=2, command=lambda: self.click("3"))
        self.b3.place_configure(x=250, y=150)


        # row 3
        self.b4 = Button(text="4", font="Arial 25", width=3, height=2, command=lambda: self.click("4"))
        self.b4.place_configure(x=50, y=250)
        
        self.b5 = Button(text="5", font="Arial 25", width=3, height=2, command=lambda: self.click("5"))
        self.b5.place_configure(x=150, y=250)

        self.b6 = Button(text="6", font="Arial 25", width=3, height=2, command=lambda: self.click("6"))
        self.b6.place_configure(x=250, y=250)


        # row 4
        self.b7 = Button(text="7", font="Arial 25", width=3, height=2, command=lambda: self.click("7"))
        self.b7.place_configure(x=50, y=350)

        self.b8 = Button(text="8", font="Arial 25", width=3, height=2, command=lambda: self.click("8"))
        self.b8.place_configure(x=150, y=350)

        self.b9 = Button(text="9", font="Arial 25", width=3, height=2, command=lambda: self.click("9"))
        self.b9.place_configure(x=250, y=350)

        self.resolver = Button(text="Resolver", font="Arial 20", width=8, height=2, command=lambda: self.solucionar())
        self.resolver.place_configure(x=800, y=370)


    def click(self, n):
        self.entrada.insert((len(self.entrada.get())), n)

    def solucionar(self):
        exp = self.entrada.get()
        x = sympy.symbols("x")
        self.resultado.configure(text=(sympy.solve(exp, x)))
                
root = Tk()
root.geometry("1000x500")
window = App(root)
window.mainloop()