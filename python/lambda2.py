
#filter
def filter_by_length(words):
       # Escribe tu solución 👇
   lisa=list(filter(lambda i: len(i)>= 4, words))
   return lisa

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response) 

numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)


matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))


#reduce 


import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)

numbers = [1, 2, 3, 4, 5]
total = functools.reduce(lambda x, y: x + y, numbers)
print(total) # Imprime 15

numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product) # Imprime 120  

words = ['hola', ' ', 'soy', 'un', 'pocoloco']
sentence = functools.reduce(lambda x, y: x + y, words)
print(sentence) # Imprime "hola soy un pocoloco"


import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)



numbers = [1, 2, 3, 4, 5]
total = functools.reduce(lambda x, y: x + y, numbers)
print(total) # Imprime 15


#calcular la suma de los números pares de un conjunto de números
numeros=[1,2,3,4,5,6,7,8,9,10]

def pares(numeros):
  return functools.reduce(lambda x, y: x + y if y % 2 == 0 else x, numeros)
print(pares(numeros))


  
#calcular la suma de los números impares de un conjunto de números
def impares(numeros):
  return functools.reduce(lambda x,y: x+y if y % 2 == 0 else y, numeros)
print(impares(numeros)) 