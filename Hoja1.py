# 1-4
saludos = "¡Hola mundo!"
print(saludos)

nombre = input("Introduce tu nombre: ")
print("¡Hola " + nombre + "!")

# 5
nombreMayus = nombre.upper()
n = len(nombre) 
print(nombreMayus + " tiene " + str(n) + " letras")

# 6
print("Cual es tu peso(kg)?")
peso = float(input())
print("Cual es tu estatura(m)?")
estatura = float(input())
imc = (peso) / (estatura) ** 2
resultado = str(round(imc, 2))
print( nombre + " tu indice de masa corporal es " + resultado)

#7
print("Dame el primer numero entero: ")
entero1 = int(input())
print("Dame el segundo numero entero: ")
entero2 = int(input())
cociente = (entero1)/(entero2)
resto = (entero1)%(entero2)
print(entero1 + " entre " + entero2 + " da un cociente " + str(cociente) + " y un resto " + str(resto))
print(divmod(entero1,entero2))

#8
CONTRASEÑA = "contraseña"
print("Introduzca su contraseña: ")
contraseña = input()
contraseñaMinu = contraseña.lower()
if (CONTRASEÑA == contraseñaMinu):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")