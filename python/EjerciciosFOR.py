'''
Realice un programa que enumere los paises de la siguiente lista
paises = ['Canada', 'USA', 'Mexico', 'Australia']


paises = ['Canada', 'USA', 'Mexico', 'Australia']

for indice, pais in enumerate(paises,start=1):
    print(f'{indice}. {pais}')

for i in range (len(paises)):
    print(f'{i+1}.{paises[i]} ')

'''


'''
Crear un ciclo for que cuente de 0 a 100
suma=0
for x in range (0,101):
    suma+=x
print(f'resultado : {suma}')

'''

'''
Haz una tabla de multiplicar utilizando el ciclo for
'''
'''
for y in range (1,11):
    for t in range(1,11):
        print(f'{y} * {t} = {y*t}')


for b in range(1,11):
    print(f'{2}*{b}= {2*b}')
    

'''


'''
Imprima los números del 1 a 10 al revés utilizando el ciclo for

lista=[]
for i in range (1,11):
    lista.append(i)
lista.reverse()
print(lista)

for j in range(10,0,-1):
    print(j)

'''


'''
Crear un bucle que cuente todos los números pares hasta el 100

suma=0
for i in range(0,101,2):
    suma+=i
print(suma)

'''

'''
Cree un bucle que sume los números del 100 al 200
suma=0
for i in range(100,201):
    suma+=i
print(suma)

'''

'''
Use un bucle para mostrar elementos de una lista dada que estén presentes en posiciones pares4
lista=[1,2,3,4,5,6,7,8,9]
for i in lista:
  if i % 2==0:
    continue
  print(i)

# Usar un bucle for para recorrer la lista y mostrar los números en posiciones pares
for i in range(1, len(numeros), 2):
    print(numeros[i])
'''

'''
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in my_list:
  if i > 0:
    new_list.append(i)
print(new_list)
'''

cantidad=int(input('cantidad de numeros: '))
promedio=[]
for i in range(cantidad):
    numero=float(input('digite el numero: '))
    promedio.append(numero)
print(promedio)

if cantidad>0:
    sumatoria=sum(promedio)/cantidad
    print(f'el resultado seria {sumatoria}')
else:
    print(f'no se puede realizar ')