from Interfaz import (menu, OpcionSeleccionada)
opcion = 0
while opcion != 3:
    op = menu
    PorcentajesNotas = OpcionSeleccionada(op)
    if PorcentajesNotas == 1:
        print ("a")
    elif PorcentajesNotas == 2:
        print ("b")
    elif PorcentajesNotas == 3:
        print ("c")
        break
else:
    print ("opcion equivocada")