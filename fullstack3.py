# Desafio desarrollador fullstack
# Importacion de librerias necesarias
import random

# Variables
vecMon = []
n = 0

# Funciones
def minCambio(vec): # Minimo cambio posible
    cambio = 1
    for i in vec:
        if i > cambio:
            break
        cambio += i
    return cambio

#Punto 3
n = random.randint(2,10) # Tamaño del vector de forma aleatoria de 2 a 15
cont = n

for i in range(0,n):    # Creacion del vector con numeros random de 0 a 100
  vecMon.append(random.randint(1,10))

vecMon.sort()           #Ordenamiento del vector
print(vecMon)

mincam = minCambio(vecMon)
print("El cambio minimo posible es ", mincam)

