sum_plata = 0
sum_edad  = 0
# sum_edad_mujer
# sum_edad_hombre
tot_menores  = 0
#sum_mayores  = 0
#   150 Personas  y 100 menores = 150 -100  = 50
tot_persona  = 0
con_hombres = 0
con_mujeres = 0
swSeguir = True
while (swSeguir):
    resGen = input("Hombre o Mujer H/M")
    resEdad = int(input("Edad"))
    tot_persona = tot_persona + 1
    sum_edad  = sum_edad + resEdad
    if resEdad < 18:
        tot_menores = tot_menores + 1
    if resGen =='H':
        con_hombres = con_hombres + 1
    else :
        con_mujeres = con_mujeres + 1
    #if resGen =='M':
        #con_mujeres = con_mujeres + 1
    res  = input("Hay Otra Persona S/N")
    #if res == "S":
    #    swSeguir = True
    #else:
    #    swSeguir = False
    if  res == "N":
        swSeguir = False


print(f"Total Persona   {tot_persona}") 
print(f"Total Hombres   {con_hombres}") 
print(f"Total Mujeres   {con_mujeres}") 
print()
print(f"Total Menores   {tot_menores}") 
print(f"Total Mayores   {tot_persona - tot_menores}") 
print(f"Total Mayores   {tot_persona - tot_menores}")
print(f"Total Mayores   {tot_persona - tot_menores}")
print(f"Total Mayores   {tot_persona - tot_menores}")
print(f"Total Mayores   {tot_persona - tot_menores}")
print(f"Total Mayores   {tot_persona - tot_menores}")
#2M


tot_mayores = tot_persona - tot_menores  #+ 5 
print(f"Total Mayores   {tot_mayores}") 
print(f"Total Mayores   {tot_mayores}") 
print(f"Total Mayores   {tot_mayores}") 
print(f"Total Mayores   {tot_mayores}") 
print(f"Total Mayores   {tot_mayores}") 
#3M