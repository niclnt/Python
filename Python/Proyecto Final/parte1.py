continuar = True
juan=0
contadorMeses=0


while continuar:
    contadorMeses=contadorMeses+1
    juan= juan + 300
    if contadorMeses >= 6:
        continuar=False

print(f"la dinero que tiene juan en junio es: {juan} USD")  
            
continuar= True
while continuar:
    contadorMeses=contadorMeses+1
    juan= juan + 500
    if contadorMeses >= 10:
        continuar=False

print(f"la dinero que tiene juan en octubre es: {juan} USD")

continuar= True
while continuar:
    contadorMeses=contadorMeses+1
    juan= juan + 700
    if contadorMeses >= 12:
        continuar=False

print(f"la dinero que tiene juan en diciembre es: {juan} USD")

promedio = juan / contadorMeses

print(f"el promedio del dinero que cobro juan es: {promedio} USD")

if promedio <= 300:
    print("el sueldo de juan es bajo")
elif promedio >= 300 and promedio <= 900:
    print("el sueldo de juan es normal")
elif promedio >= 900:
    print("juan tiene un sueldo mayor a lo normal")


