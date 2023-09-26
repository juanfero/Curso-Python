#Ejercicios moudulos 1 practica estudiantes Pipe comunica. 
#Deben realizar el ejercicio normal y con listcomprehension 

# Pregunta 1: Listas
# Dada una lista de números, crea una nueva lista que contenga solo los números pares de la lista original.

lista=[1,2,3,4,5,6,7,8,9,10,14,23,67,12,78,35,55,33,2,66,32,16,67]
'''
new_list=[]
for i in lista:
    if i %2==0:
        new_list.append(i)
        new_list.sort()
print(new_list)

'''

otra_forma=[j for j in lista if j %2==0 ]
otra_forma.sort()
print(otra_forma)


# Pregunta 2: Tuplas
# Crea una tupla que contenga los nombres de tres países de tu elección.

tupla=('colombia','chile', 'brazil')
print(type(tupla))
print(tupla)

# Pregunta 3: Diccionarios
# Dada una lista de nombres de ciudades y otra lista con la población de cada ciudad,
# crea un diccionario que relacione cada ciudad con su respectiva población.

import random
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]
poblacion = [3207247, 1620809, 791413, 688711]

diccionario=dict(zip(ciudades,poblacion))
print(diccionario)

solucion={p:random.randint(1,11) for p in ciudades}
print(solucion)

# Pregunta 4: Sets
# Dada una lista con valores duplicados, crea un set que contenga solo los valores únicos.

lista_duplicada = [1, 2, 2, 3, 4, 4, 5, 5,7,6]
grupo=set(lista_duplicada)
grupo.add(67)
print(grupo)



'''
cos={90,34,67}
conjunto.add(56)
conjunto.remove(1)
conjunto.update(cos)

print(conjunto)

for i in range(1,20):
  conjunto.add(i)
  if i ==3:
        conjunto.remove(i)


print(conjunto)

'''
conjunto=[1,6,3,4,7,0,2,5]
numeros=[2,5,3,1,6,23,8,65,3,2]
numbers=[1,3,5,7,9,11]


new_cojuntos=set(conjunto)
new_numeros=set(numeros)
new_numbers=set(numbers)
nuevos=set()
for i in (new_cojuntos , new_numeros , new_numbers):
      nuevos=new_cojuntos & new_numeros & new_numbers
      print(nuevos)
#print(new_cojuntos & new_numeros & new_numbers)

#tener un diccionario que contenga elnombre  y las notas de cada corte de la universidad, si se saca mas de 4.0 lo guaeda a una listade aprobados de lo contario lo mando a una lista de reprobados

notas = [
    {
    'nombre': 'Juan',
    'edad': 25,
    'corte1':4.7,
    'corte2':4.5,
    'corte3':4.3
    },
    {
    'nombre': 'Mario',
    'edad': 18,
    'corte1':4.2,
    'corte2':4.2,
    'corte3':3.9
    },
    {
    'nombre': 'Pedro',
    'edad': 21,
    'corte1':4.2,
    'corte2':2,
    'corte3':2
    }
]

#print(notas)
aprobados = []
for estudiante in notas:
    nombre = estudiante['nombre']
    nota=float((estudiante['corte1']+estudiante['corte2']+estudiante['corte3']) /3)
    print(f'La nota de {nombre} es {nota}')
    if nota >= 4.0:
        aprobados.append(estudiante)
        print(f'El estudiante {nombre} aprobado')
    else:
        print(f'El estudiante {nombre} reprobo')

promedio = sum(estudiante['corte1'] + estudiante['corte2']+ estudiante['corte3'] for estudiante in notas)/(3*len(notas))
print(f'la nota promedio del curso fue {promedio}')










