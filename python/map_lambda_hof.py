def suma(x):
    return x*2

def solucion(y,funcion):
    return y + funcion
print(solucion(3,suma(2)))


suma_2=lambda x:x*2

solucion_2=lambda y,funcion: y+funcion
reult=solucion_2(3,suma_2(3))
print(reult)



listas=[1,2,3,4]
listas_2=[3,5,2,8,4,1,5]

maps=list(map(lambda x: x*2,listas))
print(maps)

print(list(map(lambda y: y*2 ,listas_2)))


hola=lambda x:x*5
print(hola(4))

def ingredientes(a, b):
  return a + " es a " + b


def prueba(a,b):
  return a+b
prueba=lambda a,b: a+b

prueba_2=lambda a,funcion:a+funcion
result=prueba_2(3,prueba(2,8))
print(result)

#map


numeros=[1,5,8,6,7,2]
ndos=[1,89,6,3]

solucionado=list(map(lambda i:i*2, numeros))
print(solucionado)

sop=tuple(map(lambda i,j:i*j, numeros,ndos))
print(sop)


menu = list(map(ingredientes, ('carne', 'maiz', 'aguacate'), ('molida', 'tacos', 'guacamole')))

print(menu)

items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]
price=list(map(lambda item:item['product'], items))
print(price)

def addtaxes(i):
    i['taxes']=i['price']*.19
    return i 
newlist=list(map(addtaxes,items))
print(newlist)

edad=[
    {
        'nombre':'juan',
        'genero':'male',
        'edades': 19
    },
    {
        'nombre':'nicolle',
        'genero':'famale',
        'edades': 23

    },
    {
        'nombre':'Tita',
        'genero':'famale',
        'edades': 68

    }
]



#.copy() es para crar otra referencia en la memoria een el diccionario. 
saber=list(map(lambda i:i['edades']*2, edad))
print(saber)

import random
def agregar(j):
    j['id']=random.randint(1, 100)
    return j
aplica=list(map(agregar, edad))
print(aplica)


def multiply_numbers(numbers):
    result=list(map(lambda i:i*2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)


## 
