from customtkinter import *

app = CTk()
app.title("Adivina la palabra")
app.resizable(width=True, height=True)

def Salir ():
    app.destroy()

acciones = CTkButton(app, text="Acciones")
jugar = CTkButton(app, text="Jugar")
salir = CTkButton(app, text="Salir", command=Salir)

acciones.grid(row=0, column=0, pady=5, padx=5)
jugar.grid(row=0, column=1, pady=5, padx=5)
salir.grid(row=0, column=2, pady=5, padx=5)


app.mainloop()