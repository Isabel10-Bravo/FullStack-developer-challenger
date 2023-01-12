# Prueba para Banco de Bogota
# Importacion de librerias
import random

# Declaración de variables
vIn = []
vOut =[]
n = 15
s = 6

# Funciones
def orden(vIn):     # Re-Ordenar las posiciones del vector de atras hacia adelante
  vOut = [None] * cont
  for i in range(0,cont):
      vOut[(cont-1)-i] = vIn[i]
  print("Vector ordenado y ",vOut)

def verificar(num): # Verificar cada posicion si tiene el numero S y devuelve None
  if num < 10:      # Un solo digito
    if num == s:
      num = None
    else:
      num = num
  elif num >= 10:   # Dos digitos
    num1 = int(str(num)[0])
    num2 = int(str(num)[1])
    if num1 == s:
      if num2 == s:
        num = None
      else:
        num = num2
    else:
      if num2 == s:
        num = num1
      else: 
        num = num
  return num
  
def eliminar(vec,pos): # Reorganiza las posiciones en el vector al encontar un type None
  global cont
  cont = cont - 1
  for i in range(pos,n-1):
    vec[i] = vec[i+1]

#Punto 1
n = random.randint(2,15) # Tamaño del vector de forma aleatoria de 2 a 15
cont = n
for i in range(0,n):    # Creacion del vector con numeros random de 0 a 100
  vIn.append(random.randint(0,99))
print("Vector inicial",vIn)
for i in range(0,n):    # Llamado de las funciones para verificar y eliminar los valores en cada celda
  vIn[i] = verificar(vIn[i]) 
  if vIn[i] == None:
        eliminar(vIn,i)
orden(vIn)              # Llamado de la funcion para re-ordenar el vector



