#Clase 1 - Tuplas
numbers = (1, 2, 3, 4, 5)
strings =('camilo', 'laura', 'paula', 'carola')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

#Clase 2 - Diccionarios
my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)
#Los diccionarios se compones de llave, valor.
# muy similares a un archivo .json
my_dict = {
    'avion': 'objeto volador',
    'name': 'Javier',
    'last_name': 'Sepulveda',
    'age': 109
}

print(my_dict)

#el tamanio del diccionario
print(len(my_dict))

#imprimiendo una llave 
print(my_dict['age'])

#La funcion get, si no existe el valor sale un mensaje none(Maneja el error)
# Se cambian los corchetes por parentesis(), ya que get es una funcion de python
print(my_dict.get('test'))

print('name' in my_dict)
print('other' in my_dict)

#Clase 3 - Diccionarios insercion y actualizacion
person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())