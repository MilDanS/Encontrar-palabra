from random import *
from sqlite3 import *
from tkinter import *
from tkinter import messagebox

def lomalo ():
    baseDeDatos = connect("EncontrarPalabra.db")#SE conecta con la base de datos
    cr = baseDeDatos.cursor()

    app = Tk()#SE creo la pantalla principal
    app.title("Juego Adivina Palabra")

    Intentos = 3#variables principales
    Fallos = 0
    Word = " "
    Desc = " "

    def salir():
        app.destroy()#Funcion para salir

    def verificar ():
        global Intentos, Fallos, Word #Usa las variables globales para verificar la respuesta.

        entrada = juego.get().strip()#Obtiene el texto ingresado por el jugador y elimina espacios.

        if entrada == "":
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")#Si el campo está vacío, muestra una advertencia.
            return
        elif entrada.lower() == Word.lower():
            messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {Word}")#Si se gana, mumetra un mensaje
            juego.delete(0, END)#Limpia el espacio
        else:
            Intentos -= 1#Si es incorrecta, reduce los intentos y aumenta los fallos.
            Fallos += 1

            if Intentos > 0:#Muestra mensaje de error o derrota según los intentos restantes.
                messagebox.showinfo("Incorrecto", f"Palabra incorrecta. Te quedan {Intentos} intentos.")
                juego.delete(0, END)
            else:
                messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {Word}")
                juego.delete(0, END)

    def jugar ():
        global Intentos, Fallos, Word, Desc
        Intentos = 3#Reinicia los contadores.
        Fallos = 0

        numero = randint(1, 7)#Selecciona aleatoriamente una palabra por su id en la base de datos.
        cr.execute('''SELECT nombre, descripcion FROM palabras 
                    WHERE id = ?''', (numero, ))

        resultado = cr.fetchone()
        Word  = resultado[0]
        Desc = resultado[1]
        #Limpia el campo de entrada y muestra la nueva descripción.
        juego.delete(0, END)
        descrip.configure(text=Desc)

    juego = Entry(app)
    descrip = Label(app, text=" ")
    jugarb = Button(app, text="Jugar", command=jugar)
    int = Button(app, text="Verificar", command=verificar)
    next = Button(app, text="Salir", command=salir)

    Label(app, text="Ingresa la palabra:").grid(row=1, column=0, padx=5, pady=5)

    Label(app, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)

    juego.grid(row=1, column=0, columnspan=3, pady=5, padx=5)
    descrip.grid(row=0, column=1, pady=5, padx=5)
    jugarb.grid(row=2, column=0, pady=5, padx=5)
    int.grid(row=2, column=1,padx=5, pady=5)
    next.grid(row=2, column=2, pady=5, padx=5)

    app.mainloop()




