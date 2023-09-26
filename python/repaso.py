'''
Tema 1: Listas

    Crea una lista llamada numeros con los números del 1 al 10.
    Agrega el número 11 al final de la lista.
    Imprime el tercer elemento de la lista.
    Elimina el número 5 de la lista.
    Imprime la longitud de la lista.
'''
import random
numeros = list(range(1,11))
print(numeros)
numeros.append(11)
print(numeros)
print(numeros[2])
numeros.remove(5)
print(numeros)
print(len(numeros))

'''
Tema 2: Diccionarios

    Crea un diccionario llamado persona con las claves "nombre" y "edad", y sus valores correspondientes.
    Agrega una nueva clave-valor al diccionario para representar la "ciudad" de la persona.
    Imprime la edad de la persona.
    Elimina la clave "ciudad" del diccionario.
    Verifica si la clave "ciudad" existe en el diccionario y muestra un mensaje adecuado en función del resultado.

    tener un diccionario que contenga elnombre  y las notas de cada corte de la universidad, si se saca mas de 4.0 lo guaeda a una listade aprobados de lo contario lo mando a una lista de reprobados 
'''
notas={





}

diccionario ={
    "nombre": "Juan",
    "edad": 25,
}
print(diccionario)

diccionario['ciudad']='Bogota'
print(diccionario)

print(diccionario.get('edad'))

print(diccionario.pop('ciudad'))

if 'ciudad' in diccionario:
    print('no s e encuentra')


'''
Tema 3: Tuplas

    Crea una tupla llamada frutas con tres nombres de frutas.
    Intenta cambiar el valor de la primera fruta en la tupla y observa el error que ocurre.(las tuplas no se pueden cambiar)
    Convierte la tupla frutas en una lista y agrega una fruta adicional.
    Convierte la lista nuevamente en una tupla.
'''
frutas=('manzana', 'pera', 'banano')

new_fruts=list(frutas)
new_fruts.append('kiwi')
print(tuple(new_fruts))


'''
Tema 4: Funciones

    Crea una función llamada suma que tome dos argumentos y devuelva la suma de ellos.
    Llama a la función suma con dos números diferentes y muestra el resultado.
    Crea una función llamada saludo que tome el nombre de una persona como argumento y devuelva un saludo personalizado.
    Llama a la función saludo con tu nombre y muestra el saludo.

'''

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2
 

def solucion(x,y):
    s=suma(x,y)
    result=6*s
    return s,result

print(solucion(3,5))

def saludo (nombre):
    return f'Hola {nombre}'
print(saludo('juan'))


'''
Tema 5: Ciclos For

    Utiliza un bucle for para imprimir los números del 1 al 5.
    Utiliza un bucle for para recorrer la lista de numeros del tema 1 y muestra cada número.
'''

for i in range(1,6):
    print(i)


'''
Tema 6: Lambda

    Crea una función lambda que tome un número como argumento y devuelva su cuadrado.
    Utiliza la función lambda para calcular el cuadrado de un número.
'''

cuadrado =lambda i:i**2 
print(cuadrado(5))


'''
ema 7: Comprehensions

    Crea una lista de números pares del 1 al 10 utilizando una comprensión de lista.
    Crea una lista de los cuadrados de los números del 1 al 5 utilizando una comprensión de lista.
'''
lista=[i-1 for i in range(1,10,2)]
print(lista)

dale=[i**2 for i in range(1,6)]
print(dale)

'''
    Crea una lista de números del 1 al 5.
    Utiliza la función map para aplicar la función lambda (del tema 6) a cada elemento de la lista y obtener una lista de los cuadrados de los números.
'''

numbers=list(range(1,6))
funcion=list(map(lambda x:x**2,numbers))
    


