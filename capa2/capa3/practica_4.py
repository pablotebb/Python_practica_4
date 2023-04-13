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