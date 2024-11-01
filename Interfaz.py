#Definimos las opciones del menu
def menu ():
    print ("Bienvenido a la CALCULA DE PORCETAJES")
    print ("!!MENU¡¡\n1) Ingresar un porcentaje\n2) Ingresar una nota\n3) Salir")
    op = int(input("Ingresa una opcion: "))
    return op
#Definimos las acciones que toma cada opcion del menu
def OpcionSeleccionada (op):
    AgregarPorce = 1
    AgregarNota = 2
    Salir = 3
    if op == 1:
        print ("Usted ha seleccionada agregar nota")
        return AgregarPorce
    elif op == 2:
        print ("Usted ha elegido añadir nota")
        return AgregarNota
    elif op == 3:
        print ("Usted esta saliendo de la claculadora de notas y porcentajes, Suerte y Feliz Día")
        return Salir
    else:
        print ("La opcion es invalida o incorrecta")

#Se añade el porcentaje al array
def añadirporcentaje():
    porcentaje = {}
    return porcentaje