 # *Desafio Desarollador FullStack* 
 
 ## Programas a utilizar
 
 Para estos desafios se uso el lenguaje de programación Python, programado con la version python.3.10 
 es necesario int6alalrla para ejecutar cada uno de los desafios explicados a continuación
 
 ## Ejecución de Programas
 
 Se cuenta de tres archivos .py cada uno es el programa del desafio especifico, para la ejecución de cada programa se debe abrir una
 ventana de comando (CMD), e ingresar a la carpeta que contenga los tres archivos, para ejecutarlos se debe escribir la palabra
 *python* seguido del nombre del archivo, ejemplo para el ejercico 1 se escribe python fullstack.py 
  
 ## Desafios
 > # Codigo Hash 
 Para iniciar el desafio se genera el codigo Hash como se muestra en la imagen, para este caso el numero seleccionado es el 9
 
 ![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/bb4b65549f123f64da66f417efa0b81716f8536c/hasg%20generator.png)
 
 Este número es requerido para los primeros dos desafios, este digito se parametriza en cada codigo tal que se pueda modificar a combeniencia del usuario
 
 
> # Desafio 1
Para este desafio se importan las librerias a usar en este caso random, se crea e inicializa las variables necesarias, en el caso del vector el tamaño es
aleatorio del 2 - 15 y los digitos del vector de igual forma pero entre el rango 1 - 99. Cada valor que compone el vector se verifica el número de digitos 
para descomponerlo en unidades y descenas y simultaneamente verificar si es igual al codigo Hash para modoficarlo o eliminarlo si es necesario. 
A continuación se verifica cada celda del vector si esta vacia y de ser necesario hacer un corriento en el vector y eliminar la celda vacia, y por ultimo
se reorganiza el vector cambiando las posiciones de atras hacia adelante.

Como se menciono el tamaño del vector y los valores son generados de forma aleatorio solo es necesario ejecutar el programa desde la consola de comandos 
con el comando *python fullstack.py* e inmediatamente en la consola se imprime los dos vectores como se observa a continuación 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/3ea043faa0b474df4807334427d83bd402eb8a82/Desafio1.PNG)

El vector generado inicialmente es de 15 posiciones y en base al codigo Hash se eliminan los numeros 9, modificando unicamente el numero 59, quedando 
como 5 y de igual forma se imprime el vector ordenado

> # Desafio 2

Para este desafio se importan las librerias a usar en este caso random y math, se crea e inicializa las variables necesarias, de la misma manera que en el 
desafio 1 se crea vector con el tamaño aleatorio entre 2 - 15 y los digitos del vector aleatorios entre el rango -20 - 20. A continuación 
se ordena el vector de forma ascendente, se eleva a la potencia el vector y nuevamente se ordenan los valores del vector de forma ascendente, posteriormente 
se verifica que los valores del vector sean menor a 99, de lo contrario se elimina el valor y la celda.

De la misma manera para este desafio solo es necesario ejecutar en la venta de comandos el comando *python Fullstack2.py* y en la consolo se observa 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/6d42205fec324f12836d680e207ef14232b66a2f/Desafio2.PNG)

Se imprime cada vector, el generado aletoriamente de tres posiciones, posteriormente cada vector en cada paso, cuando se ordena de forma ascendente,
se eleva al cuadrado y se organiza nuevamente de manera ascendente, por ultimo el vector sin los valores mayores a 99, en este caso es el 400.

> # Desafio 3

Para este desafio se importan las librerias a usar en este caso random, se crea e inicializa las variables necesarias, de la misma manera que en el 
desafio 1 se crea vector con el tamaño aleatorio entre 2 - 15 y los digitos del vector aleatorios entre el rango 1 - 100 los cuales representan monedas.
A continuación se organizan las monedas de forma acsendente y por ultimo para determinar el minimo cambio que no es posible dar se itera cada posicion 
del vector comenzando con las monedas de menor denominación y asi detenrmiar el menor cambio que no es podible dar.

De la misma manera para este desafio solo es necesario ejecutar en la venta de comandos el comando *python Fullstack3.py* y en la consolo se observa 

![This is an image](https://github.com/Isabel10-Bravo/FullStack-developer-challenger/blob/a7f04b4373b61d13fa33e56d547f51a036dacac7/Desafio3.PNG)

La impresión del vector de monedas  que tiene con un tamaño 6 posiciones y por ultimo imprime el minimo cambio que es posible dar que en este caso es 27
