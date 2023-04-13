palabras = ["gato", "ventana", "cajón"]

for w in palabras:
  print(w, len(w))
  
  
usuarios = {"Pepe": "activo", "María": "inactivo", "Juan": "activo", "José": "inactivo", "Juana": "activo"}

print(usuarios)


for usuario, estatus in usuarios.copy().items():
  if estatus == "inactivo":
    del usuarios[usuario]
    
print(usuarios)


usuarios = {"Pepe": "activo", "María": "inactivo", "Juan": "activo", "José": "inactivo", "Juana": "activo"}

usuarios_activos = {}

for usuario, estatus in usuarios.items():
  if estatus == "activo":
    usuarios_activos[usuario] = estatus
    
print(usuarios_activos)


for i in range(5):
  print(i, end=" ")
  
print("\n")
  
for i in range(0, 7):
  print(i, end=" ")
  
print("\n")

for i in range(0, 7, 2):
  print(i, end=" ")
  
  
nombres = ["Pablo", "Juana", "Elena", "Julia"]

print("\n")

for indice in range(len(nombres)):
  print(f"{indice} - {nombres[indice]}")
  
print("\n")
  
for i in range(10): 
  print(i, end=" ")
  
print("\n")
  
for i in range(0, 10):
  print(i, end=" ")
  
suma = sum(range(5)) # 0, 1, 2, 3, 4

print("\n")

print(f"La suma es: {suma}")

print("\n")

for i in range(5):
  print(i, end=" ")
  
print("\n")


for num in range(2, 10):
  if num % 2 == 0:
    print(f"El numero: {num} es par")
    continue
  print(f"El numero: {num} es impar")
  
  
# while True:
#   pass 
  
  
class Mi_clase:
  pass 

mi_obj = Mi_clase()

# print(mi_obj)

def mi_funcion():
  pass 

mi_funcion()


def http_error(status):
  match status:
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


