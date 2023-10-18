num = int(input("ingrese un numero entero: "))

if num % 2 == 0:
    print("el numero " + str(num) + " es par")
else:
    print("el numero " + str(num) + " es impar")

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

if num1 < num2:
    print("el primero es menor")
elif num2 < num1:
    print("el segundo es menor")
else:
    print("los numeros son iguales")
