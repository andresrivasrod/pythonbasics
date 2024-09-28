<h1>If conditionals</h1>
En estos dos archivos de python haremos un codigo que recibe como input un numero e identifica si este es o no es un numero par. Tambien tenemos un codigo el cual simula una calculadora con diferentes funciones matematicas. Para la implementacion de estos dos codigos se usaron los condicionales if. Primero tenemos que entender que un condicional if se usa cuando para ejecutar una acción primero queremos verificar que se cumpla una condición específica, por ejemplo hay que ingresar un numero del a 1 al 3 y queremos que con cada opcion se ejecute un codigo diferente, primero verificamos si el valor ingresado es igual a 1. Tambien hay que considerar que pueden existir diferentes valores que nuestra variable puede tomar y que para cada una exista una accion diferente a tomar, es por ello que existe el "elif" que quiere decir en ingles "else if", es decir, si no es la primera condicion tambien puede ser esta siguiente, siguiendo nuestro ejemplo que el valor ingresado sea igual a 2 o a 3. Y finalmente tenemos el caso en el que se ingrese otro valor posible, para ello usamos "else", en nuestro caso seria el escenario en el que el usuario ingresa un numero que no es ni 1, 2 o 3.  Esto se vería asi:

if number == 1:
    #codigo a ejecutar si el numero ingresado es 1
elif number ==2:
    #codigo a ejecutar si el numero ingresado es 2
elif number ==3:
    #codigo a ejecutar si el numero ingresado es 3
else:
    #codigo a ejecutar si se ingresa cualquier otro numero

<h1>Operaciones Matematicas</h1>
Para estos ejercicios vamos a usar varias operaciones matematicas, es por ello que tenemos que ver como las usamos en python
<b>Sumar</b>
Para sumar usamos el simbolo "+", esto se veria por ejemplo: a = 1+2 #entonces a sera igual a 3
<b>Restar</b>
Para restar usamos el simbolo "-", esto se veria por ejemplo: a = 2-1 #entonces a sera igual a 1
<b>Multiplicar</b>
Para multiplicar usamos el simbolo "*", esto se veria por ejemplo: a = 2*2 #entonces a sera igual a 4
<b>Dividir</b>
Para dividir usamos el simbolo "/", esto se veria por ejemplo: a = 4/2 #entonces a sera igual a 2
<b>Potencia</b>
Para sacar la potencia de un numero con otro usamos "**", esto se veria por ejemplo: a = 2**3 #entonces a seria igual a 2 elevado a la 3, es decir 8
<b>Modulo</b>
El modulo es el residuo de una division entre dos numeros y para obtenerlo usamos "%", esto se veria por ejemplo:
a = 4%2 #en este caso el residuo de la division 4/2 es 0, por lo que a seria igual a 0
a = 5%2 #en este caso el residuo de la division 5/2 es 1, por lo que a seria igual a 1
<b>Comparar</b>
Podemos comparar si dos numeros son iguales "==", mayor que ">", menor que "<", mayor o igual que ">=", o menor o igual que "<="