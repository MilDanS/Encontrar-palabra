from sqlite3 import *

baseDeDatos = connect("EncontrarPalabra.db")

cr =baseDeDatos.cursor()

def tabla():
    cr.execute('''CREATE TABLE IF NOT EXISTS palabras(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL
                );''')
    baseDeDatos.commit()
tabla()


