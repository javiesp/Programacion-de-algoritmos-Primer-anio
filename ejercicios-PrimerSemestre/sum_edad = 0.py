import os

sum_edad = 0 
con_mujeres = 0 
con_hombre = 0
tot_personas = 0 
tot_menores = 0 

swContinuar = True
while (swContinuar):
    resGen = input('Himbre o mujer H/M: ')
    res_edad = input( 'edad : ')
    tot_personas = tot_personas + 1
    if sum_edad > 18: 
        tot_personas = tot_menores + 1

if resGen == 'H' :
    con_hombres = con_hombre + 1
else: 
    con_mujeres = con_mujeres + 1

res = input('hay mas personas S/N: ')

if res == 'N' : 
    swContinuar = False 
os.system ('cls')
print(f'Total perosonas;  {tot_personas}')
print(f'Total mujeres;  {con_mujeres}')
print(f'Total hombres;  {con_hombres}')
print()
print(f'Total menores;  {tot_menores}')
print(f'Total mayores;  {tot_personas}')

print()


