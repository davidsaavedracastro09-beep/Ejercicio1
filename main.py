print("Hola, bienvenidos a mi programa que va simular tu banco de confianza")
# Saldo inicial
saldo = 1000

# Lista para guardar operaciones
historial = []

# Variable para controlar el menú
opcion = 0

# Menú interactivo
while opcion != 4:

    print("CAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    # Consultar saldo
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo}")
        historial.append("Consultó saldo")

    # Depositar dinero
    elif opcion == 2:
        deposito = float(input("Ingrese el monto a depositar: $"))

