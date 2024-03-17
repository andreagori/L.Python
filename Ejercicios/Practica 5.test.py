"""
Ejercicio 30:
Comenzando con 200 bacterias, el crecimiento en el número de bacterias
después de n horas se calcula de la siguiente manera: B = 200 × 2n. Imprima la
cantidad de bacterias después de 0, 5, 10 y 15 horas en formato de tabla como
se muestra a continuación. Utilice la secuencia de escape de tabulación para
lograr el resultado de dos columnas.

"""

bacterias = int(200)
numero = int(2)
# Hora0 = int(0)
# Hora5 = int(5)
# Hora10 = int(10)
# Hora15 = int(15)

print("Horas\t\tNumero de bacterias")
# El for es diferente en python, aqui por ejemplo usando un arreglo, definimos las horas y se realizo la operacion sin necesidad de variables.
for horas in [0, 5, 10, 15]:
    total_bacterias = bacterias * (numero**horas)
    print(horas, "\t\t", total_bacterias)

print("------------------------------------")
"""
Reimplementa el script utilizando f-strings en el cual se muestra de la siguiente
manera: (los datos apoyados a la derecha)
"""
print("Horas\t\tNumero de bacterias")
for horas in [0, 5, 10, 15]:
    total_bacterias = bacterias * (numero**horas)
    print(f"{horas:>5}\t{total_bacterias:>27}")

# lo que realiza el :> es que el numero despues asigna la cantidad de espacios a la derecha, si usara <, seria a la izquierda.


"""
Ejercicio 31: (SIN BUCLE O CICLO).
Escriba un script que ingrese una cantidad de segundos desde el usuario.
Calcula el número de horas, minutos y segundos restantes. Imprímelos
separados por “-”. Por ejemplo, si el usuario escribe 3750 segundos como
entrada, el script debería imprimir:
1- 2- 30

Supongamos que el usuario ingresa una cantidad de segundos superior a 3600.
Utilice tanto la división de piso como la operación residuo para calcular la
cantidad de horas, minutos y segundos.

Ingresar tiempo en segundos: 3750
1 - 2 - 30
"""

segundosUsuario = int(input("Ingresa tiempo en segundos: "))
horas = segundosUsuario // 3600  # el doble // es para que te salga enteros.
segundosRestantes = (
    segundosUsuario % 3600
)  # esto te dara en la variable el residuo de la division. los segundos que quedan sin hacer una resta
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(f"{horas} - {minutos} - {segundos}")

"""
Ejercicio 32:
Escribió un script que calculaba la cantidad de horas, minutos y segundos
restantes en función de la cantidad de segundos recibidos a través de la
entrada del usuario. Vuelva a implementar su script para usar un bucle que en
un proceso iterativo "recoja" las horas, minutos y segundos restantes usando
los operadores // y %.
"""
segundos = int(input("Ingresa tiempo en segundos: "))
segundosRestantes = segundos

for unidad in ["Horas", "Minutos", "Segundos"]:
    if unidad == "Horas":
        valorH = segundosRestantes // 3600
        segundosRestantes = segundosRestantes % 3600
    elif unidad == "Minutos":
        valorM = segundosRestantes // 60
        segundosRestantes = segundosRestantes % 60
    else:
        valorS = segundosRestantes
        print(f"{valorH} - {valorM} - {valorS}")

"""
elif condición_2:
    # código si la condición_1 es falsa pero la condición_2 es verdadera
elif condición_3:
    # código si la condición_1 y la condición_2 son falsas pero la condición_3 es verdadera
"""

"""
Ejercicio 33:
En teoría de números, un número perfecto es un número entero positivo que
es igual a la suma de sus divisores. Los pitagóricos estudiaron por primera vez
los números perfectos, quienes pensaban que tenían propiedades místicas.
También fueron ampliamente estudiados por los griegos (incluido Euclides) por
sus propiedades numerológicas.

El número perfecto más pequeño es 6, porque 6 = 3 + 2 + 1, siendo 3, 2 y 1 los
divisores. Otros ejemplos de números perfectos son: 28, 496 y 8128. Escriba un
script que ingrese un número entero no negativo y muestre si es un número
perfecto o no.
"""

numUsuario = int(input("Ingresa un numero: "))
suma_divisores = 0
for numeros in range(
    1, numUsuario
):  # se puede usar el range cuando se desconoce los numeros, recuerda.
    if numUsuario % numeros == 0:
        suma_divisores = suma_divisores + numeros

if suma_divisores == numUsuario:
    print("El numero", numUsuario, "es un numero perfecto")
else:
    print("El numero", numUsuario, "no es un numero perfecto")

"""
Ejercicio 34:
Ingrese un número entero que contenga 0 y 1 (es decir, un número entero
“binario”) y muestre su equivalente decimal. [Sugerencia: utilice los
operadores de residuo y división(o división de piso) para seleccionar los dígitos
del número "binario" uno a la vez, de derecha a izquierda. Así como en el
sistema numérico decimal, donde el dígito más a la derecha tiene el valor
posicional 1 y el siguiente dígito a la izquierda tiene el valor posicional 10,
luego 100, luego 1000, etc., en el sistema numérico binario, el dígito más a la
derecha tiene el valor posicional 1, el siguiente dígito a la izquierda tiene el
valor posicional 2, luego 4, luego 8, etc. Por lo tanto, el número decimal 234 se
puede interpretar como 2 * 100 + 3 * 10 + 4 * 1. El decimal equivalente del
binario 1101 es 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.] NOTA: No utilizar la función
reversed().
"""

numero_binario = input("Ingrese un número binario (conteniendo solo 0s y 1s): ")

numero_decimal = 0
posicion = 1
for digito in numero_binario[::-1]:
    if digito == "1":
        numero_decimal += posicion
    posicion *= 2

print(f"El número decimal equivalente de {numero_binario} es: {numero_decimal}")
# explicacion de apoyo: (No le habia entendido hasta que investigue mas del tema).
"""
numero_binario[::-1] se utiliza para iterar sobre los dígitos del número binario de derecha a izquierda, 
lo que facilita la multiplicación por las potencias de 2 en el bucle for. Ejemplo con 1100:
Cuando convertimos un número binario a decimal, cada dígito en el número binario representa una potencia de 2, comenzando desde la derecha y aumentando en potencias de 2 a medida que avanzamos hacia la izquierda.

Por ejemplo, consideremos el número binario 1100:

El primer dígito desde la derecha (menos significativo) representa 2^0.
El segundo dígito representa 2^1.
El tercer dígito representa 2^2.
El cuarto dígito (más a la izquierda) representa 2^3.
Entonces, cuando encontramos un '1' en un determinado dígito del número binario, 
significa que debemos agregar el valor de la potencia de 2 correspondiente al número decimal final. Si encontramos un '0', simplemente lo ignoramos.
"""

"""
Ejercicio 35:
Ingrese un número(es decir, un entero positivo) y muestre su equivalente en
binario. [Sugerencia: utilice los operadores de residuo y división(o división de
piso) para seleccionar los dígitos del número entero uno a la vez, de derecha a
izquierda. Por lo tanto, el número decimal 234 se puede interpretar como 2 *
100 + 3 * 10 + 4 * 1. El decimal equivalente del binario 1101 es 1 * 8 + 1 * 4 + 0
* 2 + 1 * 1.] NOTA: No utilizar la función reversed().
"""
