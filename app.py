from flask import Flask, render_template, request, redirect
from database import conectar 

app = Flask(__name__)

# ruta principal
@app.route('/')
def inicio():
    return render_template("index.html")

# guardar usuario
@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    usuario = request.form['txtusuario']
    password = request.form['txtcontrasena']
    rolusu = request.form['txtrol']
    documento = request.form['txtdocumento']

    # conexión
    con = conectar()
    cursor = con.cursor()

    # SQL
    #============================================================================================
    sql ="SELECT docuemple FROM usuarios WHERE docuemple = %s"

    cursor.execute(sql,(documento,))
    resultado = cursor.fetchone()

    if resultado:
         print("El documento ya esta registrado")
    else:
        sql = """INSERT INTO usuarios(usuario, password, rol, docuemple)VALUES(%s, %s, %s, %s)"""
        datos = (usuario, password, rolusu, documento)
        cursor.execute(sql, datos)
        con.commit()
        print("Usuario registrado Correctamente")
      #============================================================================================
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)