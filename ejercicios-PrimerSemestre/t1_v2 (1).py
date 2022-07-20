#Tienda de juegos
#ingresar datos class
#elegir juego 
import os

class Cliente: 
        nombre = None
        rut = None 
        fono = None         
c1 = Cliente()

class Juego: 
        cod = None
        nombre = None
        valor = None 
        cantidad = None  
        total = None  
        
j1 = Juego()
j1.cod = 1
j1.nombre ='Mario'
j1.cantidad = 0
j1.valor = 60000
j1.total = 0

j2 = Juego()
j2.cod = 2
j2.nombre ='Zelda'
j2.cantidad = 0
j2.valor = 50000
j2.total = 0

j3 = Juego()
j3.cod = 3
j3.nombre ='FiFA'
j3.cantidad = 0
j3.valor = 30000
j3.total = 0



def linea(n):
    for x in range(1,n+ 1):
        print()

def newCliente():
    linea(10)
    print('                         Ingrese datos cliente')
    print()
    c1.rut = input('                           Ingrese Rut     : ')
    c1.nombre = input('                           Ingrese nombre  : ')    
    c1.fono = input('                           Ingrese Telefono: ')
    

def procesaVenta(resJuego,resCant,accion): 
    
    if resJuego == 1:
            if accion == 'comprar':
                j1.cantidad = j1.cantidad + resCant
            else:
                j1.cantidad = j1.cantidad - resCant        
    elif resJuego == 2:    
            if accion == 'comprar':
                j2.cantidad = j2.cantidad + resCant 
            else:
                j2.cantidad = j2.cantidad - resCant
    elif resJuego == 3:    
            if accion == 'comprar':
                j3.cantidad = j3.cantidad + resCant 
            else:
                j3.cantidad = j3.cantidad - resCant
        
    
    resp = input('                       Desea ' + accion + ' otro Juego S/N :')    
    if  resp == 's' or resp == 'S':
        menuJuego(accion)
    
        
        
def verBoleta():
    
    if j1.cantidad > 0:
       j1.total = j1.valor * j1.cantidad
       print()
       print (f'                             Cantidad Juegos Mario {j1.cantidad}, Total ${j1.valor}')
    if j2.cantidad > 0:
       j2.total= j2.valor * j2.cantidad
       print()
       print (f'                             Cantidad Juegos Zelda {j2.cantidad}, Total ${j2.valor}')
    if j3.cantidad > 0:
       j3.total= j3.valor * j3.cantidad
       print()
       print (f'                             Cantidad Juegos FIFA {j3.cantidad}, Total ${j3.valor}')
   
            
    totalVenta = j1.total + j2.total + j3.total
    print()
    print(f'                             Total de la venta es : {totalVenta}')
    print()
    input("                             Presione enter para continuar...")

#ini - is valid---------------------------------------------------------------------------------       
def is_valid(numb):
    try:
        int(numb)
        return True
    except ValueError:
        return False
         
#fin - is valid---------------------------------------------------------------------------------   

def menuJuego(accion):    
    while True:
            
        os.system ('cls')
        linea(10)
        print(f'Cliente : {c1.nombre}')
        print()
        print('                       Seleccione Juego')
        print()
        print('                         0 - Salir: ')
        print(f'                         1 - MarioBros ${j1.valor}: ')
        print(f'                         2 - The Legend Of Zelda ${j2.valor}: ')
        print(f'                         3 - FIFA ${j2.valor}: ')
        linea(2)  
        resJuego = input('                       Seleccione Juego : ')   
        
        if is_valid(resJuego): 
            return resJuego
            
        else: 
            print('                     Ingrese solo caracteres numericos')
            input('                     PRESIONE ENTER PARA CONTINUAR')
        
        if resJuego in (1, 2):
            resCant = int(input('                       Ingrese cantidad : ' ))
            procesaVenta(resJuego,resCant,accion)
        else:
            return resJuego
    
    
#ini - menu principal-----------------------------------------------------------------------------------------
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
    res = input('                             Seleccione Opcion : ')
    if is_valid(res):
        return res#-->retorna opcion ingresada por patalla
    else: 
        print('                          Ingrese solo caracteres numericos')
        input('                          PRESIONE ENTER PARA CONTINUAR')
        menuPrincipal()
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


