#Clase 1 - Loops While
'''
while True:
  print('se ejecuto')


counter = 0

while counter < 10:
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)

# Clase 2 - Loops For
'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])

#Clase 3 - Ciclos anidados
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0][1])

for row in matriz:
  print(row)
  for column in row:
    print(column)