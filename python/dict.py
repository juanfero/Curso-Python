ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]
poblacion = [3207247, 1620809, 791413, 688711]
#recuerda que puedes utilizar el zip 
listass=list(zip(ciudades,poblacion))
print(listass)


dic={
    'nombre':'juanfe', 
    'age':12,
    'nick':'pipe',
    'lista': [1,7,9,4,6,3,10]
}

print(dic)
print(len(dic))
print(type(dic))
print(dic['age'])
print(dic.get('age'))
print(dic.keys())
print(dic.values())
print(dic.items())
print('juanfe'in dic)
dic['nick']='pips'

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person.get()

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')

del person
print(person)

print(person)

car={
    'marca':'mazda',
    'modelo':2004,
    'cilindraje': 1600,
    'nombre':'allegro'
}

print(car)

car['nombre']='allegro'
car['usuarios']=['juan','pipe','nicolle']
car['usuarios'].append('sandra')
print(car)

print(car.get('marca'))
print(car.keys())
print(car.values())
print(car.items())

del car ['cilindraje']
car.pop('nombre')
print(car)

for x in car.values:
    print(x)

for x in car[x]:
    print(car[x])

for i,j in car.items:
    print(i,j)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇

person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
del person["age"]

print(list(person.keys()))
print(list(person.values()))


