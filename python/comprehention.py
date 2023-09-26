#LISTAS 
'''
num=[]
for i in range(1,10):
    num.append(i*2)
print(num)

lis=[j for j in range (1,12)]
print(lis)
otro=[x*5 for x in lis ]
print(otro)


#diccionarios
se=['nicolle', 'juan']
age=[23,19]
print(list(zip(se,age)))

dic={}
for i in range (1,6):
  dic[i] = i* 2
print(dic)

diccionario={i:i*2 for i in range (1,11)}
print(diccionario)
'''

import random
countries=['colombia', 'peru', 'brazil', 'chile']
 
poblacion={i:random.randint(100,400) for i in countries}
print(poblacion)

estudiantes=['nicolle','juan', 'santi']
edad={j:random.randint(12,26) for j in estudiantes}, 
print(edad)

los={x:x*8 for x in range(2,9)}
print(los)

sip={y:u for (y,u) in los.items()}
print(sip)



text='Hola Mundo'
corregido={a:a.upper() for a in text}
print(corregido)

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)







