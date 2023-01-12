# Desafio desarrollador fullstack
# Importacion de librerias necesarias
import random
import math

# Creacion de variables
vecIn = []
n = 15
ss = 99
l = 0

# Funciones
def ordenAcs (vecIn): # Ordena el vector de forma ascendente
    vecOr = [None] * n
    k = 0
    for i in range(0,n):
        temp = vecIn[i]        #recore el vector inicial
        for j in range(0,n):
            if temp >= vecIn[j]:
                k = j
                temp = vecIn[j]
        vecIn[k] = math.inf
        vecOr[i] = temp
    return vecOr
    #print("Vector ordenado",vecOr)

def eliminar(vec,pos): # Reorganiza las posiciones en el vector al encontar un type None
    vecOut = [None] * pos
    for i in range(0,pos):
      vecOut[i] = vec[i]
    print("Vector final",vecOut)

#Punto 2
n = random.randint(2,15) # Tamaño del vector de forma aleatoria de 2 a 15
for i in range(0,n):    # Creacion del vector con numeros random de 0 a 100
  vecIn.append(random.randint(-20, 20))
print("Vector inicial ",vecIn)
vecOr = ordenAcs(vecIn) # Ordeno el vector inicial de forma ascendente
print("Vector inicial ordenado",vecOr)
for i in range(0,n):    # Elevacion del vector al cuadrado
    vecOr[i] = vecOr[i]**2
vecOr2 = ordenAcs(vecOr)# Ordeno el vector inicial de forma ascendente
print("Vector elevado ordenado",vecOr2)
for i in range(0,n):    # Verifica si datos de las posiciones son mayores a ss
    if vecOr2[i] >= ss:
        l = i
        break
    l = i + 1
eliminar(vecOr2,l)      # Elimino las celdas con numeros mayores
