from datetime import datetime

# Diccionario principal
equipos = {
    "Laptop": {"disponible": True, "prestamos": []},
    "Proyector": {"disponible": True, "prestamos": []},
    "Tablet": {"disponible": True, "prestamos": []}
}


def mostrar_equipos():
    print("\n=== Equipos ===")
    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"- {nombre}: {estado}")


def registrar_prestamo():
    mostrar_equipos()
    equipo = input("Ingrese el nombre del equipo: ")

    if equipo not in equipos:
        print("El equipo no existe.")
        return

    if not equipos[equipo]["disponible"]:
        print("El equipo ya está prestado.")
        return

    usuario = input("Nombre del usuario: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    prestamo = (usuario, fecha)
    equipos[equipo]["prestamos"].append(prestamo)
    equipos[equipo]["disponible"] = False

    print("Préstamo registrado correctamente.")


def devolver_equipo():
    equipo = input("Ingrese el nombre del equipo: ")

    if equipo not in equipos:
        print("El equipo no existe.")
        return

    if equipos[equipo]["disponible"]:
        print("El equipo ya está disponible.")
        return

    equipos[equipo]["disponible"] = True
    print("Equipo devuelto correctamente.")


def ver_historial():
    print("\n=== Historial ===")
    for nombre, datos in equipos.items():
        print(f"\nEquipo: {nombre}")
        if datos["prestamos"]:
            for usuario, fecha in datos["prestamos"]:
                print(f"- {usuario} | {fecha}")
        else:
            print("Sin préstamos registrados")


def agregar_equipo():
    nombre = input("Nombre del nuevo equipo: ")

    if nombre in equipos:
        print("El equipo ya existe.")
        return

    equipos[nombre] = {"disponible": True, "prestamos": []}
    print("Equipo agregado correctamente.")


def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()