#Trabajo practico V UNLU

#Problema 1
def suma(x, y):
    print(x + y)

#Problema 2
def sumaret(x, y):
    print(x + y)
    return x + y

#Problema 3
def longitudstr(string):
    return len(string)

#Problema 4
def potencia(base, exponente):
    return base ** exponente

#Problema 5
def mayus(string):
    return string.upper()

#Problema 6



#Problema 7
def comparacion(nombre1, nombre2):
    return len(nombre1) > len(nombre2)


#Problema 9
def testpotencia():
    assert(potencia(2, 3) == 8)
    assert(potencia(3, 2) == 9)
    assert(potencia(5, 3) == 125)

    print("Paso")


#Problema 1
numerouno = input("Ingrese el primer numero: ")
numerodos = input("Ingrese el segundo numero: ")
print("La suma de esos dos numeros es lo siguiente: ")
suma(numerouno, numerodos)

#Problema 3
nombre = input("Ingrese su nombre: ")
print(f"Su nombre tiene {longitudstr(nombre)} letras")

#Problema 9
testpotencia()
