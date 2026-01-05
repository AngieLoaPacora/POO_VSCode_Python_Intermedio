from database import conectar

def leer_empleados():
    conn=conectar()
    cursor=conn.cursor()
    
    cursor.execute('''SELECT id,nombre,edad,puesto FROM empleados''')
    empleados=cursor.fetchall()
    
    if empleados: 
        print("{:<5} {:<20} {:<15}{:<20}".format("ID","Nombre","Edad","Puesto"))
        for emp in empleados:
            print("{:<5} {:<20} {:<15}{:<20}".format(emp[0],emp[1],emp[2],emp[3]))
    
    else:
        print("No hay empleados registrados")

def crear_empleado():
    conn=conectar()
    cursor=conn.cursor()
    
    nombre=input("Nombre del Empleado:")
    edad=int(input("Edad del Empleado:"))
    puesto=input("Puesto del Empleado:")
    cursor.execute('''
        INSERT INTO empleados (nombre,edad,puesto)
        values(?,?,?)
        ''',(nombre,edad,puesto))
    conn.commit()
    conn.close()
    print("Empleado Agregado Exitosamente")
    
def actualizar_empleado():
    id_empleado=int(input("ID del empleado a actualizar:"))
    nuevo_nombre=input("Nuevo nombre (dejar vacio para no cambiar):")
    nueva_edad=input("Nueva edad (dejar vacio para no cambiar):")
    nuevo_puesto=input("nuevo puesto (dejar vacio para no cambiar)")
    conn=conectar()
    cursor=conn.cursor()
    
    if nuevo_nombre:
        cursor.execute('UPDATE empleados SET nombre =? WHERE id=?', (nuevo_nombre, id_empleado))
    if nueva_edad:
        cursor.execute('UPDATE empleados SET nombre =? WHERE id=?', (nueva_edad, id_empleado))
    if nuevo_puesto:
        cursor.execute('UPDATE empleados SET nombre =? WHERE id=?', (nuevo_puesto, id_empleado))
    conn.commit()
    conn.close()
    print("Actualizado correctamente")

def eliminar_empleado():
    id_empleado=int(input("ID del empleado a eliminar:"))
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute('DELETE FROM empleados WHERE id = ?', (id_empleado,))
    conn.commit()
    conn.close()
    print("Empleado eliminado correctamente")
    
        