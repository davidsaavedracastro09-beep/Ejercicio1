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
    elif opcion == 2:
        deposito = float(input("Ingrese el monto a depositar: $"))

        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
            historial.append(f"Depositó ${deposito}")
        else:
            print("El monto debe ser mayor a 0")

    # Retirar dinero
    elif opcion == 3:
        retiro = float(input("Ingrese el monto a retirar: $"))

        if retiro <= saldo and retiro > 0:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
            historial.append(f"Retiró ${retiro}")
        elif retiro > saldo:
            print("Fondos insuficientes")
        else:
            print("Ingrese un valor válido")


