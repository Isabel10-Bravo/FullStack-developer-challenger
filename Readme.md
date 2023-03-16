 # *Desafio Desarollador FullStack* 
 
 ## Programas a utilizar
 
 Para estos desafíos se usó el lenguaje de programación Python en la version python.3.10 
 es necesario intalalrla para ejecutar cada uno de los desafios explicados a continuación
 
 ## Ejecución de Programas
 
 Se cuenta de tres archivos .py cada uno es el programa del desafio específico, para la ejecución de cada programa se debe abrir una
 ventana de comando (CMD), e ingresar a la carpeta que contenga los tres archivos, para ejecutarlos se debe escribir la palabra
 *python* seguido del nombre del archivo, ejemplo para el ejercicio 1 se escribe python fullstack.py 
  
 ## Desafíos
 > # Codigo Hash 
 Para iniciar el desafío se genera el codigo Hash como se muestra en la imagen, para este caso el número seleccionado es el 9
 
 ![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/bb4b65549f123f64da66f417efa0b81716f8536c/hasg%20generator.png)
 
 Este número es requerido para los primeros dos desafios, este dígito se parametriza en cada código tal que se pueda modificar a comveniencia del usuario
 
 
> # Desafío 1
Para este desafío se importan la librería random, se crea e inicializa las variables necesarias, en el caso del vector el tamaño es
aleatorio del 2 - 15 y los dígitos del vector de igual forma pero entre el rango 1 - 100. Cada valor que compone el vector se verifica el número de dígitos 
para descomponerlo en unidades y decenas y simultaneamente verificar si es igual o mayor al código Hash para modificarlo o eliminarlo si es necesario. 
A continuación, se verifica cada celda del vector si esta vacía y de ser necesario hacer un corrimiento en el vector, para así, eliminar la celda vacía, y por último se reorganiza el vector cambiando las posiciones de atrás hacia adelante.

Como se mencionó el tamaño del vector y los valores son generados de forma aleatoria solo es necesario ejecutar el programa desde la consola de comandos 
con el comando *python fullstack.py* e inmediatamente en la consola se imprime los dos vectores como se observa a continuación 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/3ea043faa0b474df4807334427d83bd402eb8a82/Desafio1.PNG)

El vector generado inicialmente es de 15 posiciones y con base en el codigo Hash se eliminan los numeros 9, modificando únicamente el numero 59, quedando 
como 5 y de igual forma se imprime el vector ordenado

> # Desafio 2

Para este desafio se importan las librerías a usar las cuales fueron random y math, se crea e inicializa las variables necesarias, de la misma manera que en el 
desafio 1 se crea vector con el tamaño aleatorio entre 2 - 15 y los dígitos del vector aleatorios entre el rango -20 - 20. A continuación, 
se ordena el vector de forma ascendente, se eleva a la potencia el vector y nuevamente se ordenan los valores del vector de forma ascendente, posteriormente 
se verifica que los valores del vector sean menor a 99, de lo contrario se elimina el valor y la celda.

De la misma manera para este desafío solo es necesario ejecutar en la venta de comandos el comando *python Fullstack2.py* y en la consola se observa 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/6d42205fec324f12836d680e207ef14232b66a2f/Desafio2.PNG)

Se imprime cada vector, el generado aletoriamente de tres posiciones, posteriormente cada vector en cada paso, cuando se ordena de forma ascendente,
se eleva al cuadrado y se organiza nuevamente de manera ascendente, por ultimo el vector sin los valores mayores a 99, en este caso es el 400.

> # Desafio 3

Para este desafío se importan las librerías a usar en este caso random, se crea e inicializa las variables necesarias, de la misma manera que en el 
desafio 1 se crea vector con el tamaño aleatorio entre 2 - 15 y los dígitos del vector aleatorios entre el rango 1 - 100 los cuales representan monedas.
A continuación se organizan las monedas de forma acsendente y, por último, para determinar el minimo cambio que no es posible dar se itera cada posicion 
del vector comenzando con las monedas de menor denominación y así detenrmiar el menor cambio que no es podible dar.

De la misma manera para este desafio solo es necesario ejecutar en la venta de comandos el comando *python Fullstack3.py* y en la consolo se observa 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/a7f04b4373b61d13fa33e56d547f51a036dacac7/Desafio3.PNG)

La impresión del vector de monedas  que tiene con un tamaño 6 posiciones y por ultimo imprime el mínimo cambio que es posible dar que en este caso es 27
