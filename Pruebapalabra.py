from sqlite3 import * #se importo la libreria

baseDeDatos = connect("EncontrarPalabra.db")

cr =baseDeDatos.cursor()

def tabla():#Se creo la tabla en la base de datos
    cr.execute('''CREATE TABLE IF NOT EXISTS palabras(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL
                );''')
    baseDeDatos.commit()
tabla()
