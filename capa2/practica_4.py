from enum import Enum

class Color(Enum):
  ROJO = 'rojo'
  VERDE = 'verde'
  AZUL = 'azul'
  
# color = Color(input("Selecciona tu color: 'rojo', 'azul' o 'verde "))

# match color:
#   case Color.ROJO:
#     print("Es rojo")
#   case Color.VERDE:
#     print("Es verde")
#   case Color.AZUL:
#     print("Es azul")
    
def fib(n):
  a, b = 0, 1
  while a < n:
    if a == 1597 or a == 89:
      print(a, end=" ")
    else:
      print(a, end="-")
    a, b = b, a + b
  print()
  
# fib(2000)
fib
f = fib 
f(100)

def fib2(n):
  a, b = 0, 1
  resultado = []
  while a < n:
    resultado.append(a)
    a, b = b, a + b
  return resultado

f200 = fib2(100)
print(f200)


def pregunta_correcto(frase_entrada, intentos=4, frase_final_bucle="Intentalo de nuevo!"):
  while True:
    resp = input(frase_entrada)
    if resp in ("s", "si", "S", "Si", "SI"):
      break
    if resp in ("n", "no", "N", "No", "NO"):
      print(frase_final_bucle)
      intentos = intentos - 1
      if intentos < 0:
        try:
          raise ValueError("Se te acabaron el número de intentos")
        except Exception as error:
          print(error)
          break
      continue
    
  
# pregunta_correcto("Quieres salir? (S/N) ")


def f(a, L=[]):
  L.append(a)
  return L

print(f(1))
print(f(2))
print(f(3))


def tienda(kind, *valores, **claves):
  print("--Tiene alguna", kind, "?")
  print("--Perdone, aqui tiene la", kind)
  for arg in valores:
    print(arg)
  print("" * 40)
  for kw in claves:
    print(kw, ":", claves[kw])
    
    
tienda("Coca-cola", "Gracias amigo", "Gracias gracias amigo", cliente="Antonio", dueno="Gilberto Alemán", bar="El bar de Pepito")


def concat(*args, separador="--"):
  return separador.join(args)

print(concat("USA", "Canada", "Reino Unido", "Francia"))


def saluda(nombre):
  return lambda x: x + nombre

f = saluda("Pedro")
print(f("Hola "))
print(f("holita "))
print(f("adios "))

pares = [(1, "uno"), (2, "dos"), (3, "tres"), (4, "cuatro")]
pares.sort(key=lambda par: par[1])

print(pares)


def mi_funcion():
  """
    Esta función no hace nada 
    y tiene 2 lineas
  """
  pass 

print(mi_funcion.__doc__)