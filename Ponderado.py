import os 

def limpiar():
    os.system('cls')

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



def notaAlumno():
  p1 = int(input(MAGENTA +'Introduzca porcentaje de ponderacion 1: '))
  p2 = int(input('Introduzca porcentaje de ponderacion 2: '))
  p3 = int(input('Introduzca porcentaje de ponderacion 3: '))
  input(YELLOW +'--------------------------------------------')
  if p1 and p2 and p3 > 100:
    input(RED + 'ERROR: la ponderación no puede ser mayor que 100')
    return notaAlumno()
  elif p1+p2+p3 > 100:
    input(RED + 'ERROR: la ponderación no puede ser mayor que 100')
    return notaAlumno()
  else:
    print('PONDERACIÓN : ',p1,'%')
    n1 = int(input('Introduzca nota 1: '))
    print('PONDERACIÓN : ',p1,'%')
    n2 = int(input('Introduzca nota 2: '))
    print('PONDERACIÓN : ',p1,'%')
    n3 = int(input('Introduzca nota 3: '))
    r1 = (n1*p1/100)
    r2 = (n2*p2/100)
    r3 = (n3*p3/100)
    print('Su nota de presentación es: ',round(r1+r2+r3))
    input()

def notaFinal():
  p1 = int(input(MAGENTA +'Introduzca porcentaje de ponderacion 1: '))
  p2 = int(input('Introduzca porcentaje de ponderacion 2: '))
  input(YELLOW +'--------------------------------------------')
  if p1 and p2 > 100:
    input(RED + 'ERROR: la ponderación no puede ser mayor que 100')
  if p1+p2 > 110:
    input(RED + 'ERROR: la ponderación no puede ser mayor que 100')
  else:
    print('PONDERACIÓN : ',p1,'%')
    n1 = int(input('Introduzca nota 1: '))
    print('PONDERACIÓN: ',p2,'%')
    n2 = int(input('Introduzca nota 2: '))
    r1 = (n1*p1/100)
    r2 = (n2*p2/100)
    nota = round(r1+r2)
    print('Su nota final: ',nota)
    if nota < 40:
      input(RED +'REPRUEBA :C')
    else:
      input(GREEN +'APROBADO!!! :D')
  

def Salir():
    opS = input('Desea salir del programa? [S/N]: ').upper()
    while True:
        if opS == 'N':
            menuEjecucion()
        else:
            break

def validaInput(val):
     try:      
      res = int(val)
      if res < 0:#validar valores negativos
       res = -1 
       input(RED + 'ERROR: Por favor, ingrese valores postivos.')
       return menuEjecucion()
     except ValueError:
      res = -1
      input(RED + 'ERROR: Por Favor ingrese valores numéricos.')
      return menuEjecucion()

     return res

def pantalla():
  print(CYAN +"""
            ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭━━━╮
            ┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╰╮╭╮┃
            ┃╰━╯┣━┳━━┳╮╭┳━━┳━╯┣┳━━╮╭╮╱┃┃┃┃
            ┃╭━━┫╭┫╭╮┃╰╯┃┃━┫╭╮┣┫╭╮┃╰╯╱┃┃┃┃
            ┃┃╱╱┃┃┃╰╯┃┃┃┃┃━┫╰╯┃┃╰╯┃╭╮╭╯╰╯┃
            ╰╯╱╱╰╯╰━━┻┻┻┻━━┻━━┻┻━━╯╰╯╰━━━╯
              CREADO POR: JAVIERA ESPINA
      ------------------------------------------

        [1] - NOTA PRESENTACIÓN 
        [2] - NOTA FINAL 
        [3] - SALIR 
        
        """
  )
  
def menuEjecucion():
  limpiar()
  pantalla()
  op = int(input('OP: '))
  res = validaInput(op)
  if res == 1:
    notaAlumno()
    menuEjecucion()
  if res ==2:
    notaFinal()
    menuEjecucion()
  if res == 0:
    Salir()


menuEjecucion()
