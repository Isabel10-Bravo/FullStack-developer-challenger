# Desafio desarrollador fullstack
# Importacion de librerias necesarias
import math
import random

# Declaración de variables
vIn = []

n = 15
s = 9

# Funciones
def orden(vIn,cont2):                            # Re-Ordenar las posiciones del vector de atras hacia adelante
  vOut = [None] * (cont2)
  for k in range(0,cont2):
      vOut[(cont2-1)-k] = vIn[k]
  return vOut

def verificar(num):                              # Verificar cada posicion si tiene el numero S y devuelve None
  numf = ""
  numeros = [None] * 3
  i = 0
  while num > 0:                                 # Separar el numero en digitos
    numeros[i] = num % 10
    num = math.trunc(num / 10)
    i = i + 1

  for j in range(0, i):                          # Verificando si es >= al S
    if numeros[j] >= s:
      numeros[j] = None

  l = 0                                          # Contador del While
  while l < i:                                   # Eliminando y ordenando los digitos
    if numeros[l] == None:
      i = eliminar(numeros, l, i)
    else:
      l = l + 1
  vec_Ver = orden(numeros, i)

  if i == 0:
    num = None
  else:
    for o in range(0, i):                          # Estructurando el numero
      vec_Ver[o] = repr(vec_Ver[o])
      numf = str(numf) + vec_Ver[o]
    num = int(numf)
  return num


def eliminar(vec,pos,cont1): # Reorganiza las posiciones en el vector al encontar un type None
  cont1 = cont1 - 1
  for m in range(pos,cont1):
    vec[m] = vec[m+1]
  vec.pop(cont1)
  return cont1

#Punto 1
n = random.randint(2,15) # Tamaño del vector de forma aleatoria de 2 a 15
cont = n
print("Tamaño del Vector Inicial:",n)

for i in range(0,n):    # Creacion del vector con numeros random de 0 a 100
  vIn.append(random.randint(0,100))
print("Vector inicial creado",vIn)

for i in range(0,n):    # Llamado de las funciones para verificar y eliminar los valores en cada celda
  vIn[i] = verificar(vIn[i])


a = 0                   #Contador del While
while a < cont:
  if vIn[a] == None:
    cont = eliminar(vIn, a, cont)
  else :
    a = a + 1

vOut = orden(vIn,cont)              # Llamado de la funcion para re-ordenar el vector
print("Vector ordenado ",vOut,"\n","Tamaño del vector ordenado:",cont)


