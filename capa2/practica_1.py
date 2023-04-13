print("C:\some\name")
print(r"C:\some\name")

print("""
    Type: string                Type use 
    -u                          This is -u 4
    -h                          Good by 
      """)

print(3 * "ovni" + "vete tu a saber")

texto = ("uno", "dos", "tres")

print(texto)

print(("hola "*3), "tontaina")


lenguaje = "Python"

print(lenguaje) # Python
print(lenguaje[-1]) # n
print(lenguaje[2:]) # thon
print(lenguaje[:-1]) # Pytho
print(lenguaje[:]) # Python 
print(lenguaje[::-1]) # nohtyP
print(lenguaje[2:42]) # thon

# Las cadenas de Python son inmutables 

try:
  lenguaje[0] = 'J'
except TypeError as e:
  print("Error, tipo de error: {}".format(e))
  
try:
  lenguaje[3] = "L"
except TypeError as e:
  print("Error, tipo de error: {}".format(e))
  
  
lenguaje = 'Javascript'

print(lenguaje)

lenguaje = "Python"

print(lenguaje)

print("F" + lenguaje[1:]) #Fython
print(lenguaje[:2] + "fhon") #Pyfhon 

palabra = "Supercalifragilisticoexpialidoso"

print(f"La palabra: '{palabra}' tiene {len(palabra)} letras.")

lista = ["uno", "dos", "tres"]

lista2 = [1, 2, 3]

print(lista, lista2)

print(lista[0], lista2[0])
print(lista[-2], lista2[-2])
print(lista[-2:], lista2[-2:])

print(lista[:], lista2[:])
print(lista, lista2)

print(lista, lista2)
print(lista + lista2)

cosas = ["hola", "lele", "hola", "jaja"]

print(cosas)

cosas[2] = "adios"

print(cosas)

cosas.append("ultimo")

print(cosas)

cosas.append("ovni "*3)

print(cosas)

anidada = [[0, 1, 2], ["hola", "holi", "adios"], ["holu", 2, 3, "bye"]]

print(anidada)

print(anidada[0])
print(anidada[0][0])
print(anidada[2])
print(anidada[2][3])

a, b = 0, 1

while a < 10:
  print(a, end="")
  a, b = b, a+b
  
nombre, apellidos, edad = "Benito", "De los boniatos", 35

print("\nTu nombre es {} {}, y tienes {} años".format(nombre, apellidos, edad))