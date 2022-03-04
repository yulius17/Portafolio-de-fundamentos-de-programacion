#ejercicio while

#Escribir un programa que pida ingresar un numero
#si el usuario no ingresa el numero entonces
#vuelva a pedir el numero hasta que se ingrese correctamente

num = int(input("ingrese un numero: "))
while not num.isdigit():
    print("ingrese correctamente")
    num = int(input("ingrese un numero: "))
print("programa terminado")

