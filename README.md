# Proyecto final de programación 
Nombre: Julio Guzmán Bajaña

# ¿Que es python? 
Python es un lenguaje de programación que nos permite escribir instrucciones dadas por el usuario para solucionar un problema paso a paso,  python se considera un interpretador ya que analiza cada instruccion, cada valor y cada toma de decisiones y todo esto permite ejecutar el programa las veces que sean necesarias.

# Qué es una variable?
una variable es la encargada de guardar datos que se utilizan en el codigo que estemos creando a la cual se le asigna un valor, ya sea este un valor escrito o numerico.
## Nombrando una variable
La variable al ser el encargado de guardar los valores debe tener un nombre que represente el valor que estamos guardando manteniendo algunas reglas a tomar en cuenta como por ejemplo:

° Pueden contener números, letras o carácter.

° No debe iniciar con un número.

° No debe ser una palabra que tenga significado dentro del lenguaje de programación o mejor conocido como palabras reservadas.

° Se debe escoger un nombre que represente el valor a guardar.

° No iniciar con letras mayusculas.

° No usar mas de 15 caracteres

## Asignando valores a una variable
A continuación dare algunos ejemplos de variables asignandole diferetes tipos de valores:
```python
nombre = "Julio"
edad = 19
```
Tambien al nombrar una variable se recomienda no usar la ( Ñ ) y en algunos casos se recomienda usar palabras en ingles como:
```python
year = 2022
civilstatus = soltero
```
Al asignar valores tambien existen varios metodos o tipos de asignaciones

```python
#Asignación en la misma linea:
#Para esto separamos cada variable con un punto y coma asi tendremos nuestra asignación en una misma linea

x = 2; y = 4; z = 6
a = 1; b = 2; c = 3


#Asignacion multiple:
#En este caso solo separamos los nombres con una coma 
#y el valor de la variable se coloca despues de un = en su respectivo orden

day, month, year = "Viernes", "Marzo", 2016


#Asignacion del mismo valor
#en estos casos tenemos dos variable pero nosotros sabemos que su valor es igual 
#entonces basicamente decimos que el "Largo" y el "Ancho" son iguales porque tienen el mismo valor

largo = ancho = 4
nota1 = nota2 = 6

#Asignacion de intercambio
#En este caso primero separamos como en el primer caso, luego intercambiamos estos valores y quedan separados por el = 
base = 20; altura = 40
base, altura = altura, base
```

## Operadores básicos
Ahora conociendo como dar un valor a las variables podemos empezar con operaciones basicas, dando a nuestras variables valores numericos y conociendo como se usan las operaciones basicas en python:

### Suma
su operador es `+` y en python se usa de la siguiente manera:
```python
suma = 10 + 11
print(suma)
[output] 21
```
Tambien al asignar valores a variables podemos sumar estas variables:
```python
a = 5
b = 10
suma = a + b
print(suma)
[output] 15
```
y se puede sumar mas de dos variables:
```python
a = 4 
b = 6
c = 10
suma = a + b + c
print(suma)
[output] 20
```
### Resta
su operador es `-` se usa de la siguiente manera:
```python 
a = 5
b = 4
resta = a - b
print(resta)
[output] 1
```

### Multiplicación
su operador es `*` se usa de la siguiente manera:
```python
a = 5
b = 5
multiplicacion = a * b
print(multiplicacion)
[output] 25
```
### División
su operador es `/` tambien existe la division entera el cual su operador es //
```python
a = 10
b = 2
division = a / b
print(division)
[output] 5
```
ahora una division entera:
```python
a = 11
b = 2
div_entera= a // b
print(div_entera)
[output] 6
```
### Módulo
su operador es `%` se usa asi:
```python 
a = 11
b = 2
modulo = a % b
print(modulo)
[output] 1
```

Tambien se toma en cuenta, cuando trabajamos con varias operaciones la prioridad de operadores:
```python
x = 1 + 2 * 3 - 4 / 5 ** 6
#entonces python trabaja asi
#Parentesis
#Potencia
#Multiplicación y division 
#Suma y resta
#Operadores iguales que se evaluan de derecha a izquierda
```

# Tipos de datos en Python
° Numericos

° Logicos

° Caracteres

## Integer
Enteros → int → Representan valores enteros ya sean positivos o negativos
ejemplos: 
```pythom
num1 = 1
num2 = 2
num3 = 3
edad = 19
```
## Float
Flotante   →   float    →   Representan valores que contienen numeros despues de un punto osea 
ejemplos:
```python
a = 1.5 
b = 2.6
c = 4.7
d = 5.9
```
## String
cadenas → str → son caracteres que forman palabras y se representan por comillas simples o dobles 
ejemplos:
```python
"hola mundo"
nombre = "Julio"
"Este es mi portafolio"
```

## Casting en Python
el casting es aquello que sirve y se utiliza para convertir un tipo de dato a un dato totalmente diferente  osea:

```python
int a str: str(65)
str a int: int("1034")
float a int: int(3.5)
```
## List
list en python son variables que almacenan varios tipos de datos en orden por ejemplo:
```python
lista_compras = ["huevos", "pan", "leche", "tocino", 12, 24, 36]
print(lista_compras)
[output] [huevos, pan, leche tocino, 12, 24, 36]
```
## Tuple
una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo.
```python
ejemplo = (1, "a", 1.1, 2, "b", 2.2).
print(ejemplo)
[output] (1, a, 1.1, 2, b, 2.2)
```

## Dictionary
Los diccionarios en python son un tipo de dato que se categoriza como una "colección" el cual permite guardar elementos (Clave:Valor).
Estos elementos se declaran con llaves `{}` y se separan con comas `,` y cada elemento se define con su palabra clave, este debe ser un dato no mutable y un valor cualquiera:
```python 
#se usa de la siguiente manera:
dic1={ }

#aqui creamos uno con claves y valores
dicCantidad={"banana":50,"mango":2,"sandia":15}
```
# Tomando decisiones
Para la toma de desiciones en python son necesarias ciertas palabras que nos permiten dirigir el rumbo de nuestro programa asignando una o varias condiciones.

## Sentencia if
`IF` es una estructura de control que ejecuta el programa cuando se cumpla cierta condición de dato Booleano.

## Sentencia elif
`ELIF` es la estructura que permite encadenar varias condiciones dependiendo de si se cumplen o no.

## Sentencia else
`ELSE` significa `de lo contrario` y se cumple son evaluar ninguna expresion condicional, entonces ejecuta el bloque de sentencias seguidas.


Aqui un ejemplo:
```python 
#podemos usar estas condiciones para averiguar si un numero es par o impar
#aqui hacemos que el usuario seleccione el numero a evaluar

n = int(input("ingrese un numero": ))

if n %2 == 0:
        print(n, "es par")
else: 
    print(n,"es impar")
#asi gracias a las condiciones que escogimos, el codigo resolvera si el numero que ingresa el usuario es par o impar
```
    
 
## Ciclo For
En python existe algo muy util llamado `ciclo for` el cual es una estructura de control que nos permite repetir sentencias(una serie de instrucciones) un número determinado de veces

°Al usar un ciclo for tambien usaremos la función `range` que nos permitira controlar el números de ciclos o veces que interactue el bucle for

```python
#en python seria de la siguien manera

#for i in range(n):

#en esta formula empezamos con el for y damos un rango de cuantas veces se repetira nuestra variable que seria "n"
```

A continuacion un ejemplo:
```python

#damos una variable 

n = 5

for i in range(n):
    print(i, "Hola")
[output] 0 Hola
         1 Hola
         2 Hola
         3 Hola
         4 Hola

#En este caso nuestra variable "n" es cinco entonces al ejecutar nuestro ciclo for nos arroja 5 veces el print("Hola")
#al agregar el "i" en nuestro print la funcion range cuenta desde 0 
#entonces nuestro rango es de 0 a 4 por eso al imprimir cuenta todos los valores desde el rango establecido
```

## Ciclo While
El ciclo `while` es una estructura de control o de repetición, que inician o repiten un bloque de instrucciones si se cumple una condicion o mientras se cumple cierta condicion 

Ejemplo:
```python
#Escribir un progrma que pida ingresar un numero
#si el usuario no ingresa el numero entonces
#vuelva a pedir el numero hasta que se ingrese correctamente

num = int(input("ingrese un numero: "))
while not num.isdigit():
    print("ingrese correctamente")
    num = int(input("ingrese un numero: "))
print("programa terminado")

[output] ingrese un numero: b
         ingrese correctamente
         ingrese un numero: 5
         programa terminado
```

## Break
En Python, la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.
```python
contador = 0

from contextlib import ContextDecorator


for i in range(3):
    for j in range(3):
        contador += 1
        print("i", i, "J", j)
        if contador >= 10:
            break

print("contador: ", contador)
[output]i 0 J 0
        i 0 J 1
        i 0 J 2
        i 1 J 0
        i 1 J 1
        i 1 J 2
        i 2 J 0
        i 2 J 1
        i 2 J 2
        contador:  9
```

## Continue
