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