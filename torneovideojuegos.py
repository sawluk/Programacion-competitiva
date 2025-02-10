jugadores = []  # Lista para almacenar los jugadores inscritos

while True:
    # Menú principal del sistema
    print("\nMenú de Gestión de Inscripciones")
    print("1. Registrar jugador")
    print("2. Eliminar jugador")
    print("3. Buscar jugador")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":  # Registrar jugador
        nombre = input("Ingrese el nombre del jugador: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue
        
        edad = input("Ingrese la edad del jugador: ")
        if not edad.isdigit():  # Verifica que la edad ingresada sea un número
            print("Error: La edad debe ser un número.")
            continue
        edad = int(edad)
        
        if edad < 12 or edad > 40:  # Rango de edad permitido
            print("Error: La edad debe estar entre 12 y 40 años.")
            continue
        
        # Verifica si el jugador ya está registrado
        if any(jugador["nombre"] == nombre for jugador in jugadores):
            print("Error: El jugador ya está inscrito.")
            continue
        
        jugadores.append({"nombre": nombre, "edad": edad})  # Agrega el jugador a la lista
        print("Jugador inscrito con éxito.")
    
    elif opcion == "2":  # Eliminar jugador
        nombre = input("Ingrese el nombre del jugador a eliminar: ").strip()
        buscar = False
        for jugador in jugadores:
            if jugador["nombre"] == nombre:
                jugadores.remove(jugador)  # Elimina el jugador de la lista
                print("Jugador eliminado correctamente.")
                buscar = True
                break
        if not buscar:
            print("Error: Jugador no encontrado.")

    elif opcion == "3":  # Buscar jugador
        nombre = input("Ingrese el nombre del jugador a buscar: ").strip()
        buscar = False
        for jugador in jugadores:
            if jugador["nombre"] == nombre:
                print(f"Jugador encontrado: {jugador['nombre']}, Edad: {jugador['edad']}")
                buscar = True
                break
        if not buscar:
            print("Error: Jugador no encontrado.")

    elif opcion == "4":  # Mostrar estadísticas
        if not jugadores:
            print("Error: No hay jugadores inscritos.")
            continue
        
        total_reg = len(jugadores)  # Número total de jugadores inscritos
        edad_prom = sum(jugador["edad"] for jugador in jugadores) / total_reg  # Cálculo de la edad promedio
        joven = min(jugadores, key=lambda x: x["edad"])  # Encuentra el jugador más joven
        viejo = max(jugadores, key=lambda x: x["edad"])  # Encuentra el jugador más viejo
        
        print("--- Estadísticas del Torneo ---")
        print(f"Total de jugadores inscritos: {total_reg}")
        print(f"Edad promedio: {edad_prom:.2f}")
        print(f"Jugador más joven: {joven['nombre']}, Edad: {joven['edad']}")
        print(f"Jugador más viejo: {viejo['nombre']}, Edad: {viejo['edad']}")
    
    elif opcion == "5":  # Salir del programa
        if len(jugadores) < 5:  # Verifica que haya al menos 5 jugadores antes de cerrar
            print("Error: No se puede cerrar el registro con menos de 5 jugadores.")
        else:
            print("Registro Terminado")
            break
    else:
        print("Error: Opción no válida, intente de nuevo.")
