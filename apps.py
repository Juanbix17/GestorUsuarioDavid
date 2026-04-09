from flask import Flask ,render_template,url_for,request,flash, redirect,session
from database import conectar 

#crear la app del proyecto
apps =  Flask(__name__)
apps.secret_key = "12345"

#crear ruta y mostrar el formulario
@apps.route('/')
def login():
    return render_template("login.html")
#Crear ruta de ingresar

@apps.route('/',methods=["POST"])
def login_form():

#crea variable de python user, contraseña para recibir del formulario 
    user = request.form['txtusuario']
    password  = request.form['txtcontrasena']

    #llamar la base de datos

    con = conectar()
    cursor = con.cursor()
    sql = "SELECT  *  FROM usuarios WHERE usuario=%s AND password=%s"
    cursor.execute(sql,(user,password))


    #resultado de la consulta
    user = cursor.fetchone()

    if user:
        #guardar las variables de sesion 
        session['usuario'] = user[1]
        session['rol'] = user [3]

        #rol = user[3] # Numero de columna del rol

        #if rol == rol:

        if user[3] == "administrador":
                return redirect(url_for("inicio"))
        else:
                return "Bienvenido empleado"
    else: 
        flash("Usuario y contraseña incorrecto", "danger")
        return redirect(url_for('login_form'))
    
    #validad sesion en la pagina principal
@apps.route('/inicio')
def inicio():
         
        if 'usuario' not in session:
            return redirect(url_for('login_form'))
        con = conectar()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)
        lista = cursor.fetchall()

        # Obtener la lista de empleados
        sql = "SELECT e.Id, e.DocumentoEmple, e.NombreEmple,e.ApellidoEmple, e.Cargo, e.SalarioB, e.HoraExtra, e.Bonificacion, d.nom_area AS Departamento FROM empleados e JOIN departamentos d  ON e.id_area = d.id_area"
        cursor.execute(sql)
        empleados = cursor.fetchall()
        
        cursor.execute(sql)
        departamentos = cursor.fetchall()

        return render_template('index.html',usuario=session['usuario'],user=lista, empleados=empleados, departamentos=departamentos)
#guardar usuario
@apps.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    usuario = request.form['txtusuario']
    password = request.form['txtcontrasena']
    rol = request.form['txtrol']
    documento = request.form['txtdocumento']

    con = conectar()
    cursor = con.cursor()

    sql = "INSERT INTO usuarios (usuario, password, rol, docuemple) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (usuario, password, rol, documento))
    con.commit()

    cursor.close()
    con.close()

    flash("Usuario registrado correctamente", "success")
    return redirect(url_for('inicio'))
#Guardar empleado==============================================================================================================================
@apps.route('/guardar_empleado', methods=['POST'])
def guardar_empleado():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    documento = request.form['txtdocumento']
    nombre = request.form['txtnombre']
    apellido = request.form['txtapellido']
    cargo = request.form['txtcargo']
    departamento = request.form['txtdepartamento']
    horas_extra = request.form['txthorasextra']
    bonificacion = request.form['txtbonificacion']

    con = conectar()
    cursor = con.cursor()

    sql = "INSERT INTO empleados (DocumentoEmple,NombreEmple,ApellidoEmple,Cargo,id_area,HoraExtra,Bonificacion) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (documento, nombre, apellido, cargo, departamento,horas_extra, bonificacion, ))
    con.commit()

    cursor.close()
    con.close()

    flash("Usuario registrado correctamente", "success")
    return redirect(url_for('inicio'))
#cerrar la sesion================================================================================================================================
@apps.route('/salir')
def salir():
      session.clear()
      return redirect(url_for('login_form'))
#Eliminar usuario
@apps.route('/eliminar/<int:id>')
def eliminarusu(id):
    if 'usuario' not in session:
        return redirect(url_for('login_form'))
    con = conectar()
    cursor = con.cursor()

    #buscar usuario
    sql = "SELECT rol FROM usuarios WHERE id_usuario=%s"
    cursor.execute(sql,(id,))
    usuario = cursor.fetchone()
    #validar el rol del usuario
    if usuario:
        rol = usuario[0]
        if rol == "administrador":
            flash("No se puede eliminar un usuario con rol de administrador")
            
        else:
            cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s",(id,))
            con.commit()
            flash("Usuario eliminado correctamente")
            
    cursor.close()
    con.close()
    return redirect(url_for('inicio'))    

#eliminar empleados
@apps.route('/eliminaremp/<int:id>')
def eliminaremp(id):
    if 'usuario' not in session:
        return redirect(url_for('login_form'))
    con = conectar()
    cursor = con.cursor()

    #buscar usuario
    sql = "SELECT Cargo FROM empleados WHERE id=%s"
    cursor.execute(sql,(id,))
    empleado = cursor.fetchone()
    #validar el rol del usuario
    if empleado:
        rol = empleado[0]
        if rol == "administrador":
            flash("No se puede eliminar un usuario con rol de administrador")
            
        else:
            cursor.execute("DELETE FROM empleados WHERE id=%s",(id,))
            con.commit()
            flash("Usuario eliminado correctamente")
            
    cursor.close()
    con.close()
    return redirect(url_for('inicio')) 
    
if __name__ == '__main__':
    apps.run(debug=True)