#https://replit.com/@Javiera1312/Examen#main.py| DIR: E:\\Projecto_examen
# listado colores
import os

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'
#--------------------
lrut = []
lnombre = []
lapaterno = []
lamaterno = []
ledad = []

def limpiar():
  os.system('Cls')

#https://fsymbols.com/es/generadores/carty/
def SelOp():
    print(MAGENTA + """

            ╱╱╱╭╮
            ╱╱╱┃┃
            ╭━━┫┃╭┳━╮╭┳━━┳━━╮
            ┃╭━┫┃┣┫╭╮╋┫╭━┫╭╮┃
            ┃╰━┫╰┫┃┃┃┃┃╰━┫╭╮┃
            ╰━━┻━┻┻╯╰┻┻━━┻╯╰╯
             -JAVIERA ESPINA-
    ----------------------------------
    """)
    print(BLUE + """
    [1] - REGISTRAR USUARIO 
    [2] - VER ASIENTOS
    [3] - CARACTER ESPECIAL
    [4] - BUSQUEDA USUARIO
    [5] - SALIR
    
    """
    )



def Salir():
    opS = input(BLUE + '¿Desea salir del programa? [S/N]: ').upper()
    while True:
        if opS == 'N':
            return menuPrincipal()
        if opS == 'S':
          break
        else:
            input(RED + 'ERROR: ingrese opción valida.')
            return Salir()

def SalirBusqueda():
    opS = input(BLUE + '¿Desea detener la busqueda? [S/N]: ').upper()
    while True:
        if opS == 'N':
            return Menubusca()
        if opS == 'S':
          menuPrincipal()
        else:
            input(RED + 'ERROR: ingrese opción valida.')
            return Salir()
        


lasiento =  [[1,2,3,4,5,6 ]
             ,[7,8,9,10,11,12]
             ,[13,14,15,16,17,18]             
            ]


def caraterEspecial():
    cont = 0
    caracteres = ('-')
    val = input('INGRESE VALOR: ')
    for x in val:
        if cont == 4:
            if x == '-':
                input('correcto')
            else:
                input('incorrecto')
        cont = cont+1




def mostrarAsiento():
  for x in lasiento:
      for y in x:
          print(str(y)+ " ",end="  ")
  


def registrarUser():
    rut = input(   'INGRESE RUT             : ')
    respuesta = caracterRut(rut)
    if respuesta == -1:
        registrarUser()
    else:
        nombre = input('INGRESE NOMBRE          : ').upper()
        apat = input(  'INGRESE APELLIDO PATERNO: ').upper()
        amat = input(  'INGRESE APELLIDO MATERNO: ').upper()
        input(GREEN +  'Cliente creado exitosamenete!!!')    
        lrut.append(rut)
        lnombre.append(nombre)
        lapaterno.append(apat)
        lamaterno.append(amat)
    

def mostarUser():
  if len(lrut) == 0:
    print(RED +'ERROR: no existen registros')
  else:
    cont = 0
    for user in lrut:
      
      print(f'RUT             : {user}')
      print(f'NOMBRE          : {lnombre[cont]}')
      #if lapaterno[cont] != '':
      print(f'APELLIDO PATERNO: {lapaterno[cont]}')
      #if lamaterno[cont] != '':
      print(f'APELLDIO MATERNO: {lamaterno[cont]}')
      cont = cont+1

def buscarUserRun():
    cont = 0
    print(YELLOW + 'INGRESE EL RUT POR BUSCAR')
    ingresouser = input('ingrese rut: ')
    for run in lrut:
        if run == ingresouser:
            print('USUARIO: ')
            print(f'Su usario es: {run}')
            print(f'Su nombre es: {lnombre[cont]}')
        cont = cont+1
      
def op2():
    print(YELLOW + 'USUARIO:')
    mostarUser()
    input(BLUE + 'ENTER PARA CONTINUAR')







    input(BLUE + 'ENTER PARA CONTINUAR')



def caracterRut(run):
    res = 0
    #  try:
    #   run = run.isnumeric()
    if run.isnumeric() == False:
        input(RED +'ERROR: por favor, ingrese valores numericos')
        res = -1
    if len(run) < 9:
        input(RED +'ERROR: el rut ingresado es menor a 9, por favor, ingrese un rut igual a 9')
        res = -1
    elif len(run) > 9:
        input(RED +'ERROR: el rut ingresado es mayor a 9, por favor, ingrese un rut igual a 9')
        res = -1
    #  except ValueError:
    #     input('ERROR: por favor, inserte valores numericos.')
    #     res = -1
    return res
    
       
def validaInput(val):
     try:      
      res = int(val)
    #   opciones = [1,2,3,4,5]
      if res > 5:
        res = -1
      if res < 0:#validar valores negativos
       res = -1 
       input(RED + 'ERROR: Por favor, ingrese valores del 1 al 5.')
       return menuPrincipal()
     except ValueError:
      res = -1
      input(RED + 'ERROR: Por Favor ingrese valores numéricos.')
      return menuPrincipal()

     return res


def Menubusca():
  limpiar()
  print(CYAN +'''
                  MENU BUSQUEDA
        ---------------------------------
        [1] - VER USUARIOS
        [2] - BUSCAR POR RUT
        [3] - SALIR

        ''')
  op = input('INGRESE UNA OPCION: ')
  resp = validaInput(op)
  if resp == 1:
    op2()
    menuPrincipal()
  if resp == 2:
    buscarUserRun()
    menuPrincipal()
  if resp == 3:
    SalirBusqueda()
    


def menuPrincipal():
    limpiar()
    SelOp()
    op = (input('INGRESE UNA OPCIÓN: '))
    resp = validaInput(op)
    if resp == 1:
        registrarUser()
        menuPrincipal()
    if resp == 2:
        mostrarAsiento()
        menuPrincipal()
    if resp == 3:
        caraterEspecial()
        menuPrincipal()
    if resp == 4:
      Menubusca()
      menuPrincipal()
    if resp == 5:
        Salir()


#---------------
#comienza aca el programa
menuPrincipal()
#----------------

