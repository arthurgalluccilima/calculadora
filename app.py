import sympy
from tkinter import *
from funcionalidades import *


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_configure(rowspan=4, columnspan=5)

        self.entrada = Entry(width="20", font="Arial 32")
        self.entrada.grid(row=1, column=1, padx=50, pady=50)

        self.resultado = Label(text="1.000.000.000", font="Arial 30")
        self.resultado.grid(row=1, column=5, padx=50, pady=50)


        # row 2
        self.b1 = Button(text="1", font="Arial 25", width=3, height=2, command=lambda: self.click("1"))
        self.b1.grid(row=2, column=2, padx=5, pady=5)

        self.b2 = Button(text="2", font="Arial 25", width=3, height=2)
        self.b2.grid(row=2, column=3, padx=5, pady=5)

        self.b3 = Button(text="3", font="Arial 25", width=3, height=2)
        self.b3.grid(row=2, column=4, padx=5, pady=5)


        # row 3
        self.b4 = Button(text="4", font="Arial 25", width=3, height=2)
        self.b4.grid(row=3, column=2, padx=5, pady=5)

        self.b5 = Button(text="5", font="Arial 25", width=3, height=2)
        self.b5.grid(row=3, column=3, padx=5, pady=5)

        self.b6 = Button(text="6", font="Arial 25", width=3, height=2)
        self.b6.grid(row=3, column=4, padx=5, pady=5)


        # row 4
        self.b7 = Button(text="7", font="Arial 25", width=3, height=2)
        self.b7.grid(row=4, column=2, padx=5, pady=5)

        self.b8 = Button(text="8", font="Arial 25", width=3, height=2)
        self.b8.grid(row=4, column=3, padx=5, pady=5)

        self.b9 = Button(text="9", font="Arial 25", width=3, height=2)
        self.b9.grid(row=4, column=4, padx=5, pady=5)

        self.resolver = Button(text="resolver", font="Arial 20", command=lambda: self.solucionar())
        self.resolver.grid(row=4, column=4)


    def click(self, n):
        self.entrada.insert(0, n)
        print("Added")

    def solucionar(self):
        exp = self.entrada.get()
        x = sympy.symbols("x")
        exp + "= x"
        sympy.solve(exp, x)
        print(x)


root = Tk()
root.geometry("1100x500")
window = App(root)
window.mainloop()