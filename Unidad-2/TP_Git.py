# Trabajo practico git

### Adjunto trabajo practico 1 ###
# %%
# Ejercicio 1

print("Hola mundo!")

# %%
# Ejercicio 2

nombre = input("Hola! Ingrese su nombre ")
print(f"Bienvenido {nombre} !")

# %%
# Ejercicio 3

nombre = input("Complete con su nombre: ")
apellido = input("Complete con su apellido: ")
edad = input("Complete con su edad: ")
lugar = input("Complete con su lugar de residencia: ")

print(f"Sus datos son: {nombre} {apellido} de {edad} años, residente de {lugar}.")

# %%
# Ejercicio 4

# Investigue si estaba la constante de pi al igual que en PSeint
# Encontre q se puede importar de esta forma y luego usar
from math import pi

radio = float(input("Ingrese el radio de un circulo"))

area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"Su area es: {area} y su perimetro es: {perimetro}")


# %%
# Ejercicio 5

segundos = float(input("Ingrese una cantidad de segundos y conviertalos a hora: "))

horas = segundos // 3600
minutos = (segundos % 3600) / 60

print(f"{segundos} Segundos equivale a: {horas} Hora/s y {minutos} Minuto/s.")

# %%
# Ejercicio 6

num = int(input("Ingrese un numero y veamos su tabla de multiplicación"))

print(f"{num} X 2 = {num * 2}")
print(f"{num} X 3 = {num * 3}")
print(f"{num} X 4 = {num * 4}")
print(f"{num} X 5 = {num * 5}")
print(f"{num} X 6 = {num * 6}")
print(f"{num} X 7 = {num * 7}")
print(f"{num} X 8 = {num * 8}")
print(f"{num} X 9 = {num * 9}")

# %%
# Ejercicio 7

num1 = int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese otro numero entero"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"veamos las operaciones entre {num1} y {num2}")
print(f"Su suma es: {suma}")
print(f"Su resta es: {resta}")
print(f"su multiplicacion es: {multiplicacion}")
print(f"Su division es: {division}")

# %%
# Ejercicio 8

print("Calculemos su indice de masa corporal")
altura = float(input("Ingrese su altura (m): "))
peso = float(input("Ingrese su peso (kg): "))

imc = peso / (altura ** 2)

print(f"su IMC es: {imc}")

# %%
# Ejercicio 9

print("Calculadora de Celsius a Fahrenheit")
cel = int(input("Ingrese la temperatura en grados Celsius (°C)"))

far = ((9/5) * cel) + 32

print(f"{cel}°C es igual a {far}°F")

# %%
# Ejercicio 10

num1 = float(input("Ingrese 3 numeros para calcular su promedio"))
num2 = float(input("Ingrese 2 mas"))
num3 = float(input("Ingrese 1 mas"))

promedio = (num1 + num2 + num3) / 3

print(f"Su promedio es de {promedio}")