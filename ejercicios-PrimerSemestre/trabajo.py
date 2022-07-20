import os

#declaracion variables globales
#valor de entradas--------------------------------------------------------------------------------------------
val_platea  = 25000
val_galeria = 15000
val_palco   = 10000
val_cancha  = 7500
#-------------------------------------------------------------------------------------------------------------


#Menu secundario para indicar valores de entradas
#--ini - Menu Entrada-----------------------------------------------------------------------------------------
def fnc_com_entrada():
    os.system ("cls") #-->limpiar pantalla (instruccioin ms-dos - windows)
    #linea_blanco(10) #-->metodo que imprime 10 lineas en blanco antes del menu
    print("                         TIPO DE ENTRADA")
    linea_blanco(1)
    print(f"                            0 - Volver")
    print(f"                            1 - Platea  ${val_platea}")
    print(f"                            2 - Galeria ${val_galeria}")
    print(f"                            3 - Palco   ${val_palco}")
    print(f"                            4 - Cancha  ${val_cancha}")    
   
    res = ingresa_opcion("                         Ingrese Tipo de Entrada : ",4)   
   
        
    if res == 1:
        valor = val_platea
        tipo  = 'Platea'         
    if res == 2:
        valor = val_galeria
        tipo  = 'Galeria'
    if res == 3:
        valor = val_palco
        tipo  = 'Palca'
    if res == 4:
        valor = val_cancha
        tipo  = 'Cancha'
    if res == -1:
        fnc_com_entrada()#-->si es -1 vuelve a mostrar el menu tipo de entrada
    
    #si ingresa un valor fuera de las opciones del menu, el programa se puede caer porque intenta 
    #pasar un valor que no existe y la multipicacion genera un error.
    if res in (1, 2, 3, 4):#solo procesa el valor si la opcion esta en el rango de 1 a 4
        fnc_procesa_entrada(valor,tipo) 
#fin - Menu Entrada-------------------------------------------------------------------------------------------


#ini - funciones venta entrada II-----------------------------------------------------------------------------
#esta funcion permite calcular todas las entradas, solo se debe pasar el tipo y valor de entrada
def fnc_procesa_entrada(valor,tipo):
        linea_blanco(1)
        print(f"                         Valor Entrada {tipo} : ${valor}")
        try:
            cantidad = int(input("                         Ingrese la cantidad de entradas : "))    
            valor_total = cantidad * valor  
            linea_blanco(1)
            print(f"                         Cantidad de entradas {cantidad} , Valor Total : ${valor_total}") 
            linea_blanco(1)              
            input("                         Presione enter para continuar...")  
        except:
            print("                         La Opcion ingresada no es correcta...!")
            input("                         Presione enter para continuar...")  
            fnc_com_entrada() 
#fin - funciones venta entrada II-----------------------------------------------------------------------------



#ini - funciones devolucion entrada---------------------------------------------------------------------------
def fnc_dev_entrada():
     print("Devolviendo  entradas...............................")
     input("Presione enter para continuar...")
#fin - funciones devolucion entrada---------------------------------------------------------------------------



#ini - funcion valida ingreso de opcion-----------------------------------------------------------------------
def ingresa_opcion(msg,nro_max):    
    print()    
    try:
        res_opcion = int(input(msg)) 
    except ValueError:
        print("                         La Opcion ingresada no es correcta...!")
        input("                         Presione enter para continuar...")
        res_opcion = -1#cada vez que genera un error por ingreso de caracter no valido pasa un -1
        return res_opcion     
    
    if res_opcion > nro_max:
        print("                         Error, las posibles selecciones son entre 0 y",nro_max)
        input("                         Presione enter para continuar...")
    return res_opcion
#fin - funcion valida ingreso de opcion----------------------------------------------------------------------- 

    
    
#ini - funcion imprime lineas en blanco- ---------------------------------------------------------------------
def linea_blanco(n):
    for x in range(1,n+1):
        print()
#fin - funcion imprime lineas en blanco-----------------------------------------------------------------------



#ini - menu principal-----------------------------------------------------------------------------------------
def menu_principal():
    os.system ("cls")#-->limpiar pantalla (instruccioin ms-dos - windows)
    linea_blanco(10)#-->agrega lineas en blanco, solo para presentacion por pantalla
    print("                         SISTEMA VENTA DE ENTRADAS")
    linea_blanco(1)
    print("                             0 - Salir")
    print("                             1 - Comprar Entradas ")
    print("                             2 - Devolver Entradas")
   
    res = ingresa_opcion("              Ingrese Opcion : ",2)    
    return res#-->retorna opcion ingresada por patalla
#fin - menu principal-----------------------------------------------------------------------------------------



#ini - PROGRAMA PRINCIPAL-------------------------------------------------------------------------------------
while  True:
    opc_menu = menu_principal()
    if opc_menu == 1:      
        fnc_com_entrada()
    if opc_menu == 2:      
        fnc_dev_entrada()
    if opc_menu == 0:
        break
#fin - PROGRAMA PRINCIPAL-------------------------------------------------------------------------------------    
    
