
'''
# append solo agrega un elemento. 
lista = []

# Pedir al usuario cuántos elementos desea ingresar
n = int(input("¿Cuántos elementos quieres ingresar? "))

# Llenar la lista con elementos ingresados por el usuario
for i in range(n):
    elemento = int(input(f"Ingresa el elemento {i + 1}: "))
    lista.append(elemento)
lista.count
print(lista)

lista[0]=9
print(lista)

print(lista[-1])
'''

w=2.0

m=[2,6,1,9]
numeros=[7,8,6,1,7,47,3,1,4,8 ]
print(numeros)
print(len(numeros))#tamano
print(type(numeros))
print(numeros.count(8))#cuenta la cantidad de vesces que se encuentra ese numero en la lista
numeros.insert(3,15)#en la posicion 3 agrego el numero 15
print(numeros)

numeros.pop(7)
print(numeros.pop(7))
print(numeros)

numeros.sort()
print(numeros)

list=numeros+m
print(list)

letters = ['A', 'B', 'C', 'D', 'E', 'F']
print(letters)
letters.append('G')
print(letters)

i=letters.index('A')
letters[i]='Z'
print(letters)

letters.remove('C')
print(letters)
letters.reverse()
print(letters)
letters.sort()
print(letters)

#letters.replace()
print(letters)

mi_tupla = (1, 2, 3, 4, 5)

# Convertir la tupla a una lista
#mi_lista = list((mi_tupla))

# Imprimir la lista resultante
#(mi_lista)


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


numbers=[2,7,4,1,3,9,0]
print(numbers[:-1])


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


tubla=('apple')
print(tuple)