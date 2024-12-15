# Lista de tareas vacía
tareas = []

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' añadida.")

def listar_tareas():
    if tareas:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("La lista de tareas está vacía.")

def eliminar_tarea():
    listar_tareas()
    if tareas:
        try:
            indice = int(input("Ingrese el número de la tarea a eliminar: "))
            if 1 <= indice <= len(tareas):
                tarea_eliminada = tareas.pop(indice - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def modificar_tarea():
    listar_tareas()
    if tareas:
        try:
            indice = int(input("Ingrese el número de la tarea a modificar: "))
            if 1 <= indice <= len(tareas):
                nueva_tarea = input("Ingrese la nueva descripción de la tarea: ")
                tareas[indice - 1] = nueva_tarea
                print(f"Tarea número {indice} modificada a '{nueva_tarea}'.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

while True:
    print("\n1. Añadir tarea\n2. Listar tareas\n3. Eliminar tarea\n4. Modificar tarea\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        listar_tareas()
    elif opcion == '3':
        eliminar_tarea()
    elif opcion == '4':
        modificar_tarea()
    elif opcion == '5':
        print("Saliendo de la aplicación. ¡Adiós!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

