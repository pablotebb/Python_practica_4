print('C:\some\name')
print(r'C:\some\name')

print('''
      Hola                        pepe 
      como        estas
      adios                       pepon
      ''')


print(3*"ovni "+" vete tu a saber!")

texto = (1, 2, 3, 4, 5)

print(texto)

print(3*"caca ", " carabaca")


lenguaje = "Python"

print(lenguaje)
print(lenguaje[-1])
print(lenguaje[2:])
print(lenguaje[:-1])
print(lenguaje[:])
print(lenguaje[::-1])
print(lenguaje[2:99])


# las cadenas no se pueden modificar 

try:
  lenguaje[0] = 'M'
except TypeError as e:
  print(f"Ha habido un error: {e}")
  
try: 
  lenguaje[3] = "S"
except TypeError as e:
  print(f"Ha habido un error: {e}")
  
  
lenguaje = "Cobol"

print(lenguaje)

lenguaje = "Python"

print(lenguaje)

print(f"F{lenguaje[1:]}")
print(f"{lenguaje[:2]}fhon")

palabra = "Supercalifragilisticoexpialidoso"

longitud = len(palabra)

print("la palabra: '{}' tiene {} letras".format(palabra, longitud))

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

miscelania = [1, "hola", "pepe", 2, 1, "hola"]

print(miscelania)

miscelania[5] = "adios"
miscelania[4] = 3

print(miscelania)

miscelania.append("caca")

print(miscelania)

miscelania.append(3**3)
miscelania.append("ovni "*3)

print(miscelania)

anidada = [[0, 1, 2], ["hola", "holi", "adios"], ["holu", 2, 3, "bye"]]

print(anidada)
print(anidada[0])
print(anidada[0][2])
print(anidada[2])
print(anidada[2][3])

a, b = 0, 1

while a < 10:
  print(a, end="")
  a, b = b, a+b
  
nombre, apellidos, edad = "Benito", "De los boniatos", 35

print(f"\n{apellidos}, {nombre}: {edad} años")
print("{}, {}: {} años".format(apellidos, nombre, edad))