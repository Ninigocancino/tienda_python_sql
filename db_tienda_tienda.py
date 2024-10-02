#Conectar Python con SQLite3

import sqlite3

conexion = sqlite3.connect("tienda_tienda.db")

cursor = conexion.cursor()
