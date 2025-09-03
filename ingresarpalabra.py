from sqlite3 import *
from customtkinter import *
from customtkinter import CTkTextbox

def lobueno():
    def agregarpalabra():#funcion para  agregar la palabra
        nuevap = palabra.get()#obtiene el texto ingresado en Entry.
        des = str(Descrip.get("1.0", "end"))#obtiene el texto completo del CTkTextbox.
                                #desde la primera línea y primer carácter ("1.0") hasta el final.

        cr.execute('''
                INSERT INTO palabras(nombre, descripcion)
                VALUES(?,?)''', (nuevap, des))#Inserta los valores en la tabla palabras de la base de datos.
        baseDeDatos.commit()

    def salir():#funcion para salir
        app.destroy()

    baseDeDatos = connect("EncontrarPalabra.db")#SE conecta a la base de datos
    cr =baseDeDatos.cursor()

    app = CTk()#SE crea la ventana principal
    app.title("Juego Adivina Palabra")

    neword =CTkLabel(app, text="Ingrese una palabra")#SE crearon etiquetas para guiar al usuaio
    descripcion =CTkLabel(app, text="Ingrese la descripción")

    palabra = CTkEntry(app, fg_color="white", text_color="black", width=150)#Para que el usuario pueda ingresar la palabra
    Descrip = CTkTextbox(app, width=150, height=50, fg_color="white", text_color="black")#Para que el usuario pueda ingresar la descripcion

    resul = CTkButton(app, text="Agregar", command=agregarpalabra)#Ejecuta la funcion agregar
    Salir=CTkButton(app, text="Salir", command=salir)#Ejecuta la funcion salir

    neword.grid(row=0, column=0, pady=5, padx=5)
    descripcion.grid(row=1, column=0, pady=5, padx=5)
    palabra.grid(row=0, column=1, pady=5, padx=5)
    Descrip.grid(row=1, column=1, pady=5, padx=5)
    resul.grid(row=2, column=0, pady=5, padx=5)
    Salir.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()
