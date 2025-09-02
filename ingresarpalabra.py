from sqlite3 import *
from customtkinter import *
from customtkinter import CTkTextbox

def lobueno():
    def agregarpalabra():
        nuevap = palabra.get()
        des = str(Descrip.get("1.0", "end"))

        cr.execute('''
                INSERT INTO palabras(nombre, descripcion)
                VALUES(?,?)''', (nuevap, des))
        baseDeDatos.commit()

    def salir():
        app.destroy()

    baseDeDatos = connect("EncontrarPalabra.db")
    cr =baseDeDatos.cursor()

    app = CTk()
    app.title("Juego Adivina Palabra")

    neword =CTkLabel(app, text="Ingrese una palabra")
    descripcion =CTkLabel(app, text="Ingrese la descripción")

    palabra = CTkEntry(app, fg_color="white", text_color="black", width=150)
    Descrip = CTkTextbox(app, width=150, height=50, fg_color="white", text_color="black")

    resul = CTkButton(app, text="Agregar", command=agregarpalabra)
    Salir=CTkButton(app, text="Salir", command=salir)

    neword.grid(row=0, column=0, pady=5, padx=5)
    descripcion.grid(row=1, column=0, pady=5, padx=5)
    palabra.grid(row=0, column=1, pady=5, padx=5)
    Descrip.grid(row=1, column=1, pady=5, padx=5)
    resul.grid(row=2, column=0, pady=5, padx=5)
    Salir.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()
