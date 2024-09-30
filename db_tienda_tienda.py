#Conectar Python con SQLite3

import sqlite3

conexion = sqlite3.connect("tienda_tienda.db")

cursor = conexion.cursor()

#Crear tablas en la dase de datos

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        precio REAL NOT NULL,
        cantidad_stock INTEGER NOT NULL,
        fecha_agregado TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cliente TEXT NOT NULL,
        correo TEXT NOT NULL,
        fecha_registro TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ordenes (
        id_orden INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        fecha_orden TEXT NOT NULL,
        monto_total REAL NOT NULL,
        FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detalles_orden (
        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
        id_orden INTEGER,
        id_producto INTEGER,
        cantidad INTEGER NOT NULL,
        precio_unitario REAL NOT NULL,
        FOREIGN KEY(id_orden) REFERENCES Ordenes(id_orden),
        FOREIGN KEY(id_producto) REFERENCES Productos(id_producto)
    )
''')

conexion.commit()