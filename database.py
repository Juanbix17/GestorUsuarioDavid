import mysql.connector

def conectar():
    # conectar a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa2"
    )

    if conn.is_connected():
        print("Conexión a la base de datos realizada correctamente")

    return conn

conectar()