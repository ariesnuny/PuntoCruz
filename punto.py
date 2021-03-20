from tkinter import *
from tkinter import colorchooser

ventana = Tk()
ventana.title("Punto Cruz")
ventana.config(bg="#DEDEDE")

punto = Canvas(ventana, width=601, height=511, bg="#DEDEDE")
punto.grid(column=0, row=0, columnspan=2)

def color1(event):
    current = event.widget.find_withtag("current")
    item = current[0]
    punto.itemconfigure(item, fill=color, outline=color)

def color2(event):
    current = event.widget.find_withtag("current")
    item = current[0]
    punto.itemconfigure(item, fill="Ghost White", outline="#DEDEDE")

def nuevo():
    cuadricula()

color = "Blue Violet"
def paleta():
    global color
    c = colorchooser.askcolor()
    color = c[1]
    boton1.configure(bg=color)

def guardar():
    punto.postscript(file="Punto_Cruz.eps")

boton1 = Button(ventana, height=2, bg=color, bd=0, cursor="hand2", command=paleta)
boton1.grid(column=0, row=1, columnspan=2, pady=2, sticky=E+W)

boton2 = Button(ventana, text="Guardar", height=2, cursor="hand2", command=guardar)
boton2.grid(column=0, row=2, sticky=E+W)

boton3 = Button(ventana, text="Nuevo", height=2, cursor="hand2", command=nuevo)
boton3.grid(column=1, row=2, sticky=E+W)

def cuadricula():
    for y0 in range(2,500,15):
        for x0 in range(2,600,15):
            for y1 in range(2,600,15):
                for x1 in range(2,600,15):
                  cua = punto.create_rectangle(15, 15, 15, 15, fill="Ghost White", width=1, outline="#DEDEDE")
                  punto.tag_bind(cua, "<Button-1>", color1)
                  punto.tag_bind(cua, "<Button-3>", color2)

cuadricula()

ventana.mainloop()