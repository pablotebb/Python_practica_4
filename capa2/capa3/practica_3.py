cadenas = ["gato", 12, "perro", 1234, "joya"]

print(len(cadenas))

cadenas = ["gato", "12", "perro", "1234", "joya"]

for elemento in cadenas:
  print(elemento, len(elemento))
  
alumnos =  {"Berta": "suspenso", "Juan": "sobresaliente", "María": "aprobado", "Noemi": "suspenso", "Candelaria": "suspenso", "Pablo": "sobresaliente"}

print(alumnos)

for clave, valor in alumnos.copy().items():
  if valor == "suspenso":
    del alumnos[clave]
    
print(alumnos)

for clave, valor in alumnos.copy().items():
  if valor is not "sobresaliente":
    del alumnos[clave]
    
print(f"Lisado de los mejores alumnos: {alumnos}")


alumnos =  {"Berta": "suspenso", "Juan": "sobresaliente", "María": "aprobado", "Noemi": "suspenso", "Candelaria": "suspenso", "Pablo": "sobresaliente"}

print(alumnos)

sobresalientes = {}

print(dir(sobresalientes))

for clave, valor in alumnos.items():
  if valor == "sobresaliente":
    sobresalientes[clave] = valor
   
print(sobresalientes)
  
  
for i in range(5):
  print(i, end=" ")
  
print("\n")

for i in range(0, 7):
  print(i, end=" ")
  
print("\n")

for i in range(0, 7, 2):
  print(i, end=" ")
  
print("\n")

nombres = ["Pablo", "Juana", "Elena", "Julia"]

for i in range(len(nombres)):
  print("{} - {}".format(i, nombres[i]))
  
  
print("\n")

for i in range(9):
  print(i, end=" ")
  
print("\n")

for i in range(0, 9):
  print(i, end=" ")
  
  
suma = sum(range(5))

print("\n")

print("la suma es: ", suma)

print("\n")

for i in range(9):
  if i % 2 == 0:
    print("El numero {} es: par".format(i))
    continue 
  print("El numero {} es: impar".format(i))
  

# while True:
#   pass 

class Mi_clase:
  pass 

mi_obj = Mi_clase()

# print(mi_obj)

def mi_funcion():
  pass 

mi_funcion()

def http_error(error):
  match error:
    case 400:
      return "Bad request"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case 500 | 501 | 502:
      return "Not allowed"
    case _:
      return "Something's wrong with the internet"
    
print(http_error(400))