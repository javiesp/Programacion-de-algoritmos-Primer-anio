#Tienda de juegos
#ingresar datos class
#elegir juego 
from msilib.schema import ReserveCost
import os

#clase cliente----------------
class cliente: 
        rut = None 
        nombre = None
        direccion = None
        comuna = None
        correo = None
        edad = None               
        fono = None
        tipo = None         
c1 = cliente()
#------------------------------

#clase juegos---------------------------------------------
class juego: 
    def __init__(self, cod, nom, can, val, tot):
        self.cod = cod
        self.nombre = nom
        self.cantidad = can 
        self.valor = val      
        self.total = tot           

j1 = juego(1 , 'Mario', 0, 60000, 0)        
j2 = juego(2 , 'Zelda', 0, 50000, 0) 
j3 = juego(3 , 'Fifa', 0, 30000, 0) 
j4 = juego(4 , 'Barbie', 0, 30000, 0) 
j5 = juego(5 , 'Pelota', 0, 30000, 0) 
j6 = juego(6 , 'Auto', 0, 30000, 0) 
j7 = juego(7 , 'Camion', 0, 30000, 0) 
j8 = juego(8 , 'Leon', 0, 30000, 0) 
j9 = juego(9 , 'Audifonos', 0, 30000, 0) 
j10 = juego(10 , 'Bicicleta', 0, 30000, 0) 

lista_de_juegos = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10]#<--se crea lista de juegos
#--------------------------------------------------------


#ini - agrega lineas en blanco--------    
def linea(n):
    for x in range(1,n+ 1):
        print()
#fin - agrega lineas en blanco--------    


#ini - ingresa cliente--------------------------------------------------------------------------------------------    
def newCliente():
    
    os.system ('cls')
    linea(5)
    print('                         Ingrese datos cliente')
    print()
    res = ingresa_rut()#funcion para validar rut  
    if res == 0:#si el usuario no quiere continuar regresa al menu principal
        return
    c1.nombre = input('                           Ingrese nombre           : ')    

    c1.direccion = input('                           Ingrese Direccion        : ')
    c1.comuna = input('                           Ingrese Comuna           : ')     
    res = ingresa_mail()#funcion para validar correo     
    if res == 0:#si el usuario no quiere continuar regresa al menu principal
        return
    res = ingresa_edad()#funcion para validar mayor de edad
    if res == 0:#si el usuario no quiere continuar regresa al menu principal
        return
    c1.fono = input('                           Ingrese Telefono         : ')
    res = ingresa_tipo()#funcion para validar tipo de cliente       
    if res == 0:#si el usuario no quiere continuar regresa al menu principal
        return
#ini - ingresa cliente--------------------------------------------------------------------------------------------           


#ini - valida rut--------------------------------------------------------------------------------------------    
def ingresa_rut():
    rut = input('                               Ingrese Rut           : ')  
    try:
        entero = int(rut)
    except:
        print()
        print("                             El rut ingresado no es correcto ")
        resp = input('                             Desea continuar ?  S/N :')
        if  resp == 's' or resp == 'S':
            ingresa_rut() 
        else:
            return 0
    	
    if entero >= 5000000 and entero <= 99999999:
        c1.rut = rut 
    else:
        print()
        print("                             El rut ingresado no es correcto ")
        resp = input('                             Desea continuar ?  S/N :')
        if  resp == 's' or resp == 'S':
            ingresa_rut() 
        else:
            return 0
        
#fin - valida rut-------------------------------------------------------------------------------------------- 


#ini - valida mail--------------------------------------------------------------------------------------------    
def ingresa_mail():
    correo = input('                           Ingrese Correo           : ')  
    if '@' in correo: #valida si existe el caracter @ en el correo ingresado por el usuario
        c1.correo = correo #si existe lo asigna al cliente
    else:#si no existe 
        print()
        print("                             El correo ingresado no es correcto, debe contener '@' ")
        resp = input('                             Desea continuar ?  S/N :')#pregunto si quiere continuar, la persona podria no tener mail    
        if  resp == 's' or resp == 'S':#si desea continuar
            ingresa_mail() #pide nuevamente el correo
        else:
            return 0
        
#fin - valida mail--------------------------------------------------------------------------------------------    
           
    
    
        
#ini - valida edad--------------------------------------------------------------------------------------------    
def ingresa_edad():
    edad = input('                           Ingrese Edad             : ')
    if int(edad) >= 18:
        c1.edad = edad
    else:
        print()
        print("                             El cliente debe ser mayor de 18 años")
        resp = input('                              Desea continuar ?  S/N :')    
        if  resp == 's' or resp == 'S':
            ingresa_edad()
        else:
           return 0
            
#fin - valida edad--------------------------------------------------------------------------------------------    




#ini - valida tipo--------------------------------------------------------------------------------------------    
def ingresa_tipo():
    tipo = input('                           Ingrese Tipo Cliente (P : Preferencial - H : Habitual - O : Ocasional) : ')
    if tipo in ('P','H','O'):
        c1.tipo = tipo
    else:
        print()
        print("                             La Opcion ingresada no es correcta")
        input("                             Presione enter para continuar...")
        resp = input('                             Desea continuar ?  S/N :')    
        if  resp == 's' or resp == 'S':
            ingresa_tipo() 
        else:
            return 0  
               
#fin - valida tipo--------------------------------------------------------------------------------------------   




#ini - Procesa venta--------------------------------------------------------------------------------------------   
def procesaVenta(resJuego,resCant,accion): 
    
    for juego in lista_de_juegos:
        if juego.cod == int(resJuego):
            if accion == 'comprar':
                 juego.cantidad = juego.cantidad + resCant
            else:
                 juego.cantidad = juego.cantidad - resCant        
    
     
    resp = input('                       Desea ' + accion + ' otro Juego S/N :')    
    if  resp == 's' or resp == 'S':
        menuJuego(accion)
#fin - procesa venta--------------------------------------------------------------------------------------------       
        
        
        


#ini - ver boleta-----------------------------------------------------------------------------------------------               
def verBoleta():
    totalVenta  = 0
    
    for juego in lista_de_juegos:
        if juego.cantidad > 0:
           juego.total =  juego.valor * juego.cantidad
           totalVenta  = totalVenta + juego.total
           print()
           print (f'                             Cantidad de {juego.nombre} {juego.cantidad}, Total ${juego.valor}')    
    print()
    print(f'                             Total de la venta es : {totalVenta}')
    print()
    input("                             Presione enter para continuar...")
#fin - ver boleta-----------------------------------------------------------------------------------------------               





#ini - menu juergo-----------------------------------------------------------------------------------------------               
def menuJuego(accion):   
    
    menuJ = {'0','1','2','3','4','5','6','7','8','9','10'}#lista - arreglo, valida que solo se ingrese uno de estos valores
    
    os.system ('cls')
    linea(5)
    print(f'Cliente : {c1.nombre}')
    print()
    print('                       Seleccione Juego')
    print()
    
    #---------en este ciclo for recorro los juegos de la lista
    #---------para mostrar por pantalla y el usuario pueda seleccionar
    for juego in lista_de_juegos:
        print('                  ' + str(juego.cod) + ' - ' + juego.nombre)
    #-------------------------------------------------------------------
     
    linea(2)   
    resJuego = input('                       Seleccione Juego : ')
       
    if resJuego in menuJ:  
        if resJuego != '0':
           resCant = int(input('                       Ingrese cantidad : ' ))
           procesaVenta(resJuego,resCant,accion)
    else:
        print("")   
        print("")
        print("                         La opcion seleccionada no es valida...")   
        input("                         Presione enter para continuar...") 
        menuJuego(accion)
#fin - menu juego -----------------------------------------------------------------------------------------------                   
    
    
    
    
#ini - menu principal-----------------------------------------------------------------------------------------
def menuPrincipal():
    
    menuP = {'0','1','2','3','4'}#lista - arreglo, valida que solo se ingrese uno de estos valores
    
    os.system ("cls")#-->limpiar pantalla (instruccioin ms-dos - windows)
    linea(5)#-->agrega lineas en blanco, solo para presentacion por pantalla
    print("                         SISTEMA TIENDA DE JUGUETES")
    linea(1)
    print("                             0 - Salir")
    print("                             1 - Ingresar Cliente ")
    print("                             2 - Comprar Juego ")
    print("                             3 - Devolver Juego")   
    print("                             4 - Ver Boleta")   
    print()
    
    res = input('                             Seleccione Opcion : ')
    
    if res in menuP:      
     return res#-->retorna opcion ingresada por patalla
    else:
     print("")   
     print("")
     print("                         La opcion seleccionada no es valida...")   
     input("                         Presione enter para continuar...")  
#fin - menu principal-----------------------------------------------------------------------------------------



while True: 
    
   res = menuPrincipal()
   
   if res == '0':
       break
   if res == '1':
       newCliente()       
   if res == '2':
       menuJuego('comprar')
   if res == '3':
       menuJuego('devolver')
   if res == '4':
       verBoleta()


