cifras = ["22", "233", "1", "12232"]

for numero in cifras:
  print(numero, len(numero))
  
usuarios = {"Pepe": "activo", "María": "inactivo", "Juan": "activo", "Jose": "inactivo", "Juana": "activo"}

print(usuarios)

for clave, valor in usuarios.copy().items():
  if valor == "inactivo":
    del usuarios[clave]
    
print(usuarios)


usuarios = {"Pepe": "activo", "María": "inactivo", "Juan": "activo", "Jose": "inactivo", "Juana": "activo"}

print(usuarios)

usuarios_activos = {}

for clave, valor in usuarios.items():
  if valor == "activo":
    usuarios_activos[clave] = valor
    
print(usuarios_activos)

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
  print(i, "-", nombres[i])
  
print("\n")

for i in range(9):
  print(i, end=" ")

print("\n")

for i in range(0, 9):
  print(i, end=" ")  


suma = sum(range(5))

print("\n")

print("la suma es {}".format(suma))

print("\n")

for num in range(0, 9):
  if num % 2 == 0:
    print(f"El número {num} es par")
    continue 
  print(f"El numero {num} es impar") 
  
  
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
    
print(http_error(404))
    