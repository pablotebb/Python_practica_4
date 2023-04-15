from enum import Enum

class Color(Enum):
  ROJO = 'rojo'
  VERDE = 'verde'
  AZUL = 'azul'
  
# color =  Color(input("Selecciona tu color: 'rojo', 'verde' o 'azul' "))

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

f22 = fib2(100)
print(f22)


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
    
  
pregunta_correcto("Quieres salir? (S/N) ")


def escritor(nombre, *datos, **frases):
  print("Hola como estas:", nombre)
  for dato in datos:
    print(dato)
  for frase in frases:
    print(frase, ") Tu frase es:", frases[frase])
    
escritor("Leon Tolstoi", "nacistes en Rusia", "tenías barba", "eras cristiano y te gustaba ayudar a la gente", frase_1 = "aquí iria la frase1", frase2= "aquí iria la frase2", frase3="aquí iria la frase3")


def concat(*args, sep="**"):
  return sep.join(args)


print(concat("Uno", "Dos", "Tres", "Juan", "Periquito", "y", "Andres"))


def multiplica(mi_constante):
  return lambda x: x * mi_constante

f = multiplica(40)
print(f(1))
print(f(2))
print(f(3))

pares = [(1, "uno"), (2, "dos"), (3, "tres"), (4, "cuatro")]
pares.sort(key=lambda par: par[1])

print(pares)


def mi_funcion():
  """
    Esta función no hace nada 
    y además
    tiene 3 lineas
  """
  pass

print(mi_funcion.__doc__)