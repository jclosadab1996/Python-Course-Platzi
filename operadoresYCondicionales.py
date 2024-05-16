# Clase 1 - Operadores
print(10 + 10)
print(10 - 5)
print(10 * 2)
print(10 / 2) # 5
print(10 % 2) # 0
print(10 / 3)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)
print(2 ** 3)
print((7 / 1) // 4)

print(8 + 3 - 1)
print(10 / 0)

print('Hola' + ' mundo')
print('Hola' * 3)

# Clase 2 - Comparacion de operadores
# > 
print(7 > 3)
print(3 > 7)
print(7 > 7)

# <
print(5 < 6)
print(6 < 5)
print(5 < 5)

# >=
print(2 >= 1)
print(2 >= 3)
print(2 >= 2)

# <=
print(1 <= 2)
print(2 <= 1)
print(2 <= 2)

# ==

print(6 == 6)
print(5 == 2)

# !=

print(6 != 10)
print(6 != 6)

print("Apple" == 'Apple')
print("Apple" == 'apple')
print("1" == 1)

age = 15
print(age >= 18)

# Clase 3 - Floats
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

print('*' * 10)

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)

# clase 4 - And & Or
# and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

role = input('Digita el rol => ')

print(role == 'admin' or role == 'seller')

# clase 5 - Not operador
print(not True) # // False
print(not False) #// True

# and
print('NOT AND')
print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and True =>', not (False and True))
print('not False and False =>', not (False and False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))

# Clase 6 - Condicionales
if True:
  print('deberia ejecutarse')

if False:
  print('nunca se ejecuta')

# pet = input('Â¿CuÃ¡l es tu mascota favorita? ')

# if pet == 'perro':
#   print('genial tienes buen gusto')
# elif pet == 'gato':
#   print('espero tengas suerte')
# elif pet == 'pez':
#   print('eres lo maximo')
# else:
#   print('no tienes ninguna mascota interesante')


# stock = int(input('Digita el stock => '))

# if stock >= 100 and stock <= 1000:
#   print('el stock es correcto')
# else:
#   print('el stock es incorrecto')


number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')