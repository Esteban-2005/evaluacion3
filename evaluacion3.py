import os
def limpiar_pantalla():
    os.system('cls')

menu = '''
1.Registrar vehiculo
2.Listar todos los vehiculos registrados
3.Imprimir orden de reparacion
4.salir
'''
marcas = ['Toyota','Ford','Chevrolet']
lista_vehiculos = []

def registrar_vehiculo():
    while True:
        limpiar_pantalla()
        try:
            print("Registrar vehiculo\n")
            marca = input("Ingrese la marca del vehiculo ('Toyota','Ford','Chevrolet'): ")
            año_de_fabricacion = int(input("ingrese año de fabricacion: "))
            kilometraje = float(input("Ingrese kilometraje del vehiculo: "))
            costo = int(input("Ingrese valor de reparacion estimada: "))
            impuesto_de_servicio = costo * 0.08
            costo_total = costo + impuesto_de_servicio

            vehiculo = {
                "marca": marca,
                "año_de_fabricacion": año_de_fabricacion,
                "kilometraje" : kilometraje,
                "costo" : costo,
                "impuesto_de_servicio" : impuesto_de_servicio,
                "costo_total" : costo_total
            }
            lista_vehiculos.append(vehiculo) 

            print("\nVehiculo registrado correctamente.\n")

            agregar_otro = input("¿Desea agregar otro? (s / n)").lower()
            if agregar_otro != 's':
                break
            else:
                print("Porfavor ingrese datos validos")
        except:
            print("Error, Debe ingresar un valor numerico. Presione enter para continuar")

def listar_vehiculos():
    limpiar_pantalla()
    input("\nListado de vehiculos registrados:\n")
    if not lista_vehiculos:
        print("No hay vehiculos registrados")
    else:
        for i, vehiculo in enumerate(lista_vehiculos, 1):
            input(f"{i}. Marca: {vehiculo['nombre']}, Año de fabricacion: {vehiculo['año_de_fabricacion']}, kilometraje: {vehiculo['kilometraje']}, "
            f"Reparacion : {vehiculo['costo']}, Impuesto de servicio: {vehiculo['impuesto_de_servicio']}, "
            f"Precio a Pagar: {vehiculo['costo_total']}")
             
        print("/nPresione enter para continuar...")




def imprimir_orden_de_reparacion():
    limpiar_pantalla()
    print("Orden de reparacion\n")
    opcion = input("Desea imprimir la orden de reparacion para todos los vehiculos (T) o por marca en especifco (M)?: ")
    if opcion == "T":
        nombre_archivo = "orden_reparacion_todos.txt"
        with open(nombre_archivo, "w")as archivo:
            for vehiculo in lista_vehiculos:
                archivo.write(f"Marca: {vehiculo['nombre']}, Año de fabricacion: {vehiculo['año_de_fabricacion']}, kilometraje: {vehiculo['kilometraje']}, "
                            f"Reparacion : {vehiculo['costo']}, Impuesto de servicio: {vehiculo['impuesto_de_servicio']}, "
                            f"Costo a Pagar: {vehiculo['costo_total']}")
             
                print(f"Orden de reparacion creada en {nombre_archivo}")

                input("Presione enter para continuar \n")

    elif opcion == "M":
       print("Lista de marcas disponibles" , ' , '.join(marcas))
       marca_seleccionada = input("Ingrese la marca del vehiculo para imrpimir su orden de reparacion: ").upper()
       marcas = [marcas for marcas in lista_vehiculos if marcas['marcas'].upper() == marca_seleccionada ]
       nombre_archivo = f"orden_reparacion_{marca_seleccionada}.txt"
    if marca_seleccionada:
        nombre_archivo = f"orden_{marca_seleccionada}.lower().replace(' ', '_').txt"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"Orden de reparacion - Marca: {marca_seleccionada}\n\n")
        for vehiculo in lista_vehiculos:
            archivo.write(f"Marca: {vehiculo['nombre']}, Año de fabricacion: {vehiculo['año_de_fabricacion']}, kilometraje: {vehiculo['kilometraje']}, "
                            f"Reparacion : {vehiculo['costo']}, Impuesto de servicio: {vehiculo['impuesto_de_servicio']}, "
                            f"Costo a Pagar: {vehiculo['costo_total']}")
            
            print(f"Orden de reparacion creada en {nombre_archivo}")

    else:
      print(f"No hay vehiculos registrados para la marca '{marca_seleccionada}'.\n")

    input("Presione enter para continuar \n")
                
                
                              

            
while True:
    limpiar_pantalla()
    print(menu)
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            registrar_vehiculo()
        elif opc == 2:
            listar_vehiculos()
        elif opc == 3:
            imprimir_orden_de_reparacion()
        elif opc == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Presione enter para continuar.")
    except:
        print("Error: Opcion invalida. Presione enter para continuar.")


