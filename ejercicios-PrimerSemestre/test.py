import os 


def linea(n):
    for x in range(1,n+ 1):
        print()

def menuPrincipal():
    os.system ("cls")#-->limpiar pantalla (instruccioin ms-dos - windows)
    linea(5)#-->agrega lineas en blanco, solo para presentacion por pantalla
    print("                         SISTEMA VENTA DE VIDEO JUEGOS")
    linea(1)
    print("                             0 - Salir")
    print("                             1 - Ingresar Cliente ")
    print("                             2 - Comprar Juego ")
    print("                             3 - Devolver Juego")   
    print("                             4 - Ver Boleta")   
    print()
    res = int(input('                             Seleccione Opcion : '))     
    return res#-->retorna opcion ingresada por patalla