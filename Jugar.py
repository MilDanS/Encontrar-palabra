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

def verificar ():
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

def jugar ():
    global Intentos, Fallos, Word, Desc
    Intentos = 3
    Fallos = 0

    numero = randint(1, 7)
    cr.execute('''SELECT nombre, descripcion FROM palabras 
                WHERE id = ?''', (numero, ))

    resultado = cr.fetchone()
    Word  = resultado[0]
    Desc = resultado[1]

    juego.delete(0, END)
    descrip.configure(text=Desc)

juego = Entry(app)
descrip = Label(app, text=" ")
jugarb = Button(app, text="Jugar", command=jugar)
int = Button(app, text="Verificar", command=verificar)

juego.grid(row= 5, column=5, pady=5, padx=5)
descrip.grid(row= 6, column=5, pady=5, padx=5)
jugarb.grid(row= 7, column=5, pady=5, padx=5)
int.grid(row=8, column=5,padx=5, pady=5)


app.mainloop()




