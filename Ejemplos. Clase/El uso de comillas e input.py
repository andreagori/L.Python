# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 07:41:56 2024

@author: andyt
"""
unaVariable = 3

# cuando el texto es muy largo 
print('Esta es una cadena mas larga, se separa asi \
lol')

# Funcion que regresa el tipo de dato
type(unaVariable) # te dira el tipo de dato

# EJERCICIO QUE MOSTRARIA COMO SALIDA ESTO:

print('int(5.2)', 'truncates 5.2 to', int(5.2))
#resultado: int 5.2, truncates 5.2 to 5

# cosas que NO puedes hacer
# print('Escribiremos 'hola' de nuevo')
# formca CORRECTA de hacerlo
print('Hola \'como\' estas')

cadena_entreComillas = """Esta es una
cadena entre comillas triples que abarca dos lineas"""
print(cadena_entreComillas)
type(cadena_entreComillas)

# funcion integral input, ingresas tu una cadena.
nombre = input("Cual es tu nombre: \n")
print(nombre)

valor = input("Ingresa un valor: \n")
int(valor)
# Otra forma de hacerlo
valorNuevo = int(input("Ingresa un valor: \n"))
print(valor, valorNuevo)

# Mini Ejercicio

numero = 6.2
float(numero)
resultado = numero * 3.3
print(resultado)
# Otra manera de hacerlo
print(float('6.2') * 3.3)

# Encadenamiento de comparaciones
value = 7
4<= value <= 12 

#Ejercicios 
5 >( 7 == False)
5 > 7 == False 
5 > 0 == False 
5 > (1== True)
5 < 1 == True 
5 > 2 == True

#codigo_python_1.py
"""Comparar números enteros usando sentencias if y operadores de comparación."""

print('Ingrese dos números enteros y te diré', 'las relaciones que satisfacen.')

#lee el primer entero
numero1 = int(input('Ingrese el primer número entero: '))

#Lee el segundo entero
numero2 = int(input('Ingrese el segundo número entero: '))

if numero1 == numero2:
    print(numero1, 'es igual a', numero2)
    
if numero1 != numero2:
    print(numero1, 'no es igual a', numero2)
    
if numero1 < numero2:
    print(numero1, 'es menor que', numero2)
    
if numero1 > numero2:
    print(numero1, 'es mayor que', numero2)
    
if numero1 <= numero2:
    print(numero1, 'es menor o igual que', numero2)

if numero1 >= numero2:
    print(numero1, 'es mayor o igual que', numero2)


print((5 > 9 == (False)))
print((5 < 9 == (True)))
print((5 == 9 < (False)))
print((9 > 5 == True))
print((9 == (5 == False)))
print((9 < 5 == True))