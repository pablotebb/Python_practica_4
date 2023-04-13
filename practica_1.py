print('C:\some\name')
print(r'C:\some\name')

print("""\
  Usage: thingy [OPTIONS]
    -h              Display this use message
    -H  hostname    Hostname to connect to 
      
      """)


print(3 * 'un' + 'uim')


text = ('Hola mundo bonito', 'como estás', 'eres lo mejor')

print(text)


print(("ium"*3), "ium")

lenguaje = "Python"

print(lenguaje)
print(lenguaje[-1])
print(lenguaje[2:])
print(lenguaje[:-1])
print(lenguaje[:])
print(lenguaje[::-1])
print(lenguaje[2:42])

# Las cadenas de Python no se pueden modificar, son inmutables
try:  
  lenguaje[0] = 'J' 
except TypeError as e:
  print(f"Error, tipo de error: {e}")
  
try:  
  lenguaje[3] = 'L'
except TypeError as e:
  print(f"Error, tipo de error: {e}")
  
  
lenguaje = "Javascript"

print(lenguaje)

lenguaje = "Python"

print(lenguaje)


print("F" + lenguaje[1:])
print(lenguaje[0:2] + "fhon")


palabra = "Supercalifragilisticoexpialidoso"

print(len(palabra))


lista = ["uno", "dos", "tres"]

lista2 = [1, 2, 3, 4]

print(lista, lista2)

print(lista[0], lista2[0])
print(lista[-2], lista2[-1])
print(lista[-2:], lista2[-2:])

print(lista[:], lista2[:])
print(lista, lista2)

print(lista, lista2)
print(lista + lista2)


cubos = [56, 12, 56, 89]

print(cubos)

cubos[2] = 13

print(cubos)

cubos.append(99)

print(cubos)

cubos.append(7**3)

print(cubos)


anidada = [[0, 1, 2], ["hola", "holi", "adios"], ["holu", 2, 3, "bye"]]

print(anidada)

print(anidada[0])
print(anidada[0][1])
print(anidada[2])
print(anidada[2][3])


a, b = 0, 1

while a < 10:
  print(a)
  a, b = b, a+b
  

nombre, apellido, edad = "Benito", "De los boniatos", 35

print(f"Tu nombre es: {nombre} {apellido}, y tienes {edad} años")