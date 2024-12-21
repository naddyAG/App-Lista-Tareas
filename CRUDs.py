import streamlit as st
import mysql.connector

def conectar_bd():
    conn = mysql.connector.connect(
        host='localhost',
        user='tu_usuario',
        password='tu_contraseña',
        database='tu_base_de_datos'
    )
    return conn

# Funciones CRUD
def crear_registro(nombre, edad):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    cursor.close()
    conn.close()

def leer_registros():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def actualizar_registro(id, nuevo_nombre, nueva_edad):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE registros SET nombre=%s, edad=%s WHERE id=%s", (nuevo_nombre, nueva_edad, id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_registro(id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registros WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

# Interfaz de Streamlit
def main():
    st.title("CRUD con Streamlit de NADYA ARANIBAR :female-technologist:")
    
    menu = ["Crear", "Leer", "Actualizar", "Eliminar"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Crear":
        st.subheader("Crear un nuevo registro")
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=1)
        if st.button("Crear"):
            crear_registro(nombre, edad)
            st.success(f"Registro creado: {nombre}, {edad}")
    
    elif choice == "Leer":
        st.subheader("Leer registros")
        resultados = leer_registros()
        for fila in resultados:
            st.write(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")
    
    elif choice == "Actualizar":
        st.subheader("Actualizar un registro")
        id = st.number_input("ID", min_value=1)
        nuevo_nombre = st.text_input("Nuevo Nombre")
        nueva_edad = st.number_input("Nueva Edad", min_value=1)
        if st.button("Actualizar"):
            actualizar_registro(id, nuevo_nombre, nueva_edad)
            st.success(f"Registro actualizado: ID {id}, Nombre: {nuevo_nombre}, Edad: {nueva_edad}")
    
    elif choice == "Eliminar":
        st.subheader("Eliminar un registro")
        id = st.number_input("ID a eliminar", min_value=1)
        if st.button("Eliminar"):
            eliminar_registro(id)
            st.success(f"Registro eliminado: ID {id}")

if __name__ == "__main__":
    main()
