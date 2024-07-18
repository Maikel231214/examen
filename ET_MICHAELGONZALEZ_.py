import random

# Lista de empleados
empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
             "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para asignar sueldos aleatorios
def asignar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in empleados]
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    menores_800 = [sueldo for sueldo in sueldos if sueldo < 800000]
    entre_800_y_2000 = [sueldo for sueldo in sueldos if 800000 <= sueldo <= 2000000]
    superiores_2000 = [sueldo for sueldo in sueldos if sueldo > 2000000]
    return menores_800, entre_800_y_2000, superiores_2000

# Función para ver estadísticas
def ver_estadisticas(sueldos):
    total_sueldos = sum(sueldos)
    num_empleados = len(sueldos)
    sueldo_promedio = total_sueldos / num_empleados
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    return {
        "total_sueldos": total_sueldos,
        "sueldo_promedio": sueldo_promedio,
        "sueldo_maximo": sueldo_maximo,
        "sueldo_minimo": sueldo_minimo
    }

# Función para generar reporte de sueldos con descuentos
def reporte_sueldos(empleados, sueldos):
    print(f"{'Empleado':<20} {'Sueldo Bruto':>15} {'Descuento Salud':>15} {'Descuento AFP':>15} {'Sueldo Neto':>15}")
    print("="*80)
    for empleado, sueldo in zip(empleados, sueldos):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_neto = sueldo - descuento_salud - descuento_afp
        print(f"{empleado:<20} ${sueldo:>14,.2f} ${descuento_salud:>14,.2f} ${descuento_afp:>14,.2f} ${sueldo_neto:>14,.2f}")

# Menú principal
def menu():
    sueldos_empleados = []
    
    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sueldos_empleados = asignar_sueldos()
            print("Sueldos asignados aleatoriamente.")
        elif opcion == "2":
            if sueldos_empleados:
                menores_800, entre_800_y_2000, superiores_2000 = clasificar_sueldos(sueldos_empleados)
                print("Sueldos clasificados:")
                print(f"Menores a $800.000: {menores_800}")
                print(f"Entre $800.000 y $2.000.000: {entre_800_y_2000}")
                print(f"Superiores a $2.000.000: {superiores_2000}")
            else:
                print("Primero debe asignar sueldos.")
        elif opcion == "3":
            if sueldos_empleados:
                estadisticas = ver_estadisticas(sueldos_empleados)
                print(f"Total sueldos: ${estadisticas['total_sueldos']}")
                print(f"Sueldo promedio: ${estadisticas['sueldo_promedio']:.2f}")
                print(f"Sueldo máximo: ${estadisticas['sueldo_maximo']}")
                print(f"Sueldo mínimo: ${estadisticas['sueldo_minimo']}")
            else:
                print("Primero debe asignar sueldos.")
        elif opcion == "4":
            if sueldos_empleados:
                reporte_sueldos(empleados, sueldos_empleados)
            else:
                print("Primero debe asignar sueldos.")
        elif opcion == "5":
            print("Finalizando programa...")
            print("Desarrollado por Michael González")
            print("RUT: 16.394.072-8")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()