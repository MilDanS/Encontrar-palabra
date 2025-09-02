from customtkinter import *
from ingresarpalabra import *
from Jugar import *

app = CTk()
app.title("Adivina la palabra")
app.resizable(width=True, height=True)

def Salir ():
    app.destroy()

acciones = CTkButton(app, text="Acciones", command=lobueno)
jugar = CTkButton(app, text="Jugar", command=lomalo)
salir = CTkButton(app, text="Salir", command=Salir)

acciones.grid(row=0, column=0, pady=5, padx=5)
jugar.grid(row=1, column=0, pady=5, padx=5)
salir.grid(row=2, column=0, pady=5, padx=5)


app.mainloop()