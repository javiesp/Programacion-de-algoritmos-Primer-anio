import json
import os
#rut=[]
import CLPersona as fnPer
import CLJuguete as fnJug
import CLBillete as fnBil


lPersona = []
lJuguete = []
lBillete = []
"""
p1 = fnPer.Persona("1","Harrys jajaja")
p2 = fnPer.Persona("2","pepito")
p1.nombre= "harrys"
print(p1.direccion)
print(p2.direccion)
"""
                    

def    loadJson():
    print("hola loadJson")
    with open ('jugueteriaJson.json', 'r') as filData:
        data = json.load(filData)         
    #print(data)
    for cliente in data["clientes"]:
        p1=fnPer.Persona(  cliente["rut"]
                    ,cliente["nombre"]
                    ,cliente["direccion"]
                    ,cliente["comuna"]
                    ,cliente["correo"]
                    ,cliente["edad"]
                    ,cliente["celular"]
                    ,cliente["tipo"]
                    )
        lPersona.append(p1)
    for juguete in data["juguetes"]:
        j1=fnJug.Juguete( juguete["codigo"]
                    ,juguete["nombre"]
                    ,juguete["cantidad"]
                    ,juguete["valor"]
                    )

        lJuguete.append(j1)
    for billete in data["billetes"]:    
        b1=fnBil.Billete(billete['codigo'],billete['cantidad'])
        lBillete.append(b1)    

def menuJuguete():
    for x in lJuguete:
        print(x.codigo,x.nombre,x.cantidad,x.valor)
    op = input("Ingrese su Opcion ")
    return op
def    saveJson():
    print("hola saveJson")
def buscaRut(stRut):
    for per in lPersona:
        print(per.rut,stRut)
        if per.rut == stRut:
            return per
    return None
def crearVenta():
    rut = int(input("Ingrese Su Rut : "))
    clsRut = buscaRut(rut)
    if clsRut == None:
        nombre  = input("Ingrese Su Nombre : ")
        direccion  = input("Ingrese Su Direccion : ")
        edad  = int(input("Ingrese Su Edad : "))
        clsRut=fnPer.Persona(  rut
                    ,nombre
                    ,direccion
                    ,'Puente Asalto'
                    ,'H@h.cl'
                    ,edad
                    ,'928282'
                    ,'M'
                    )
        lPersona.append(clsRut)
    else:
        print(clsRut.nombre,clsRut.direccion,clsRut.edad)
        input("Presione Ente Para Continuar")
    while True:
        opJuguete= menuJuguete()
        if opJuguete == "NN":
            print(" Usted ha comprado")
            for codJug in clsRut.lCodigoJueguete:
                for jug in lJuguete:
                    if (codJug == jug.codigo):
                        print(codJug,jug.codigo,jug.nombre,jug.cantidad,jug.valor)
            input("Presione Ente Para Continuar Jueguete")
            return
        clsRut.lCodigoJueguete.append(opJuguete)


#------------------------------------------------------------------
#menu Principal
#------------------------------------------------------------------
def menuPrincipal():
    while True:
        os.system ("cls")
        
        opMenu = input("""
        Menu Principal - Jugueteria
        1. Venta
        2.Consultar Productos por Cliente
        3.Consultar Total de Ventas
        0.Salir
            
        Ingresar Opcion:  """).strip()
        
        if opMenu.isnumeric() and int(opMenu) < 4:
            option = int(opMenu)
            if option == 1:
                crearVenta()  
            elif option == 2:
                listaVentasCliente()  
            elif option == 3:
                listaVentasTotal()  
            elif option == 0:                
                return
            #print("La opcion ingresada no es valida...")


def procesoPrincipal():
    loadJson()
    """
    for pp in lPersona:
        print("hola Prin", pp.nombre)

    for pp in lJuguete:
        print("hola Jugeute", pp.nombre)
    """
    menuPrincipal()    

    saveJson()






procesoPrincipal()