from sqlite3 import *
from tkinter import *

def agregarpalabra():
    nuevap = palabra.get()
    des = str(Descrip.get("1.0", "end"))
    verpalabra.configure(text=f"La palabra es: {nuevap}")
    verdes.configure(text=f"La descripción es: {des}")


    cr.execute('''
            INSERT INTO palabras(nombre, descripcion)
            VALUES(?,?)''', (nuevap, des))
    baseDeDatos.commit()

baseDeDatos = connect("EncontrarPalabra.db")
cr =baseDeDatos.cursor()

app = Tk()
app.title("Juego Adivina Palabra")

neword =Label(app, text="Ingrese una palabra")
descripcion =Label(app, text="Ingrese la descripción")

palabra = Entry(app)
Descrip = Text(app, width=15, height=3)

verpalabra= Label(app, text="La palabra es: ")
verdes = Label(app, text="La descrpción es: ")

resul = Button(app, text="Agregar", command=agregarpalabra)

neword.grid(row=0, column=0, pady=5, padx=5)
descripcion.grid(row=1, column=0, pady=5, padx=5)
palabra.grid(row=0, column=1, pady=5, padx=5)
Descrip.grid(row=1, column=1, pady=5, padx=5)
resul.grid(row=2, column=0, pady=5, padx=5)
verpalabra.grid(row=3, column=0, padx=5, pady=5)
verdes.grid(row=4, column=0, padx=5, pady=5)

app.mainloop()