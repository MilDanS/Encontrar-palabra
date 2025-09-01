from random import *
from sqlite3 import *
from tkinter import *
from tkinter import messagebox

baseDeDatos = connect("EncontrarPalabra.db")
cr = baseDeDatos.cursor()

app = Tk()
app.title("Juego Adivina Palabra")

Intentos = 3
Fallos = 0
Word = " "
Desc = " "

def jugar ():
    global Intentos, Fallos

    entrada = juego.get().strip()

    if entrada == " ":
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")
        return
    elif entrada.lower() == Word.lower():
        messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {Word}")
    else:
        Intentos -= 1
        Fallos += 1

        if Intentos > 0:
            messagebox.showinfo("Incorrecto", f"Palabra incorrecta. Te quedan {Intentos} intentos.")
            juego.delete(0, END)
        else:
            messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {Word}")
            juego.delete(0, END)

juego = Entry(app)
descrip = Label(app, text=" ")
jugarb = Button(app, text="Jugar", command=jugar)


app.mainloop()




