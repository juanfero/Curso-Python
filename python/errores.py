# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) != 4  #es una forma de verificar que una condición es cierta y, si no lo es, generar una excepción de AssertionError. 

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')# este ejecuta qu existe una exccepcion ala hora de generarla 

print('Hola 2')


'''
try 	Permite probar un bloque de código en búsqueda de un error.
except 	Permite manejar el tipo de error en el bloque.
else 	Permite ejecutar el código cuando no hay ningún tipo de error en el bloque.
finally 	Permite ejecutar el código en el bloque, independiente en el resultado de los bloques de prueba y excepción
assert() hace una verificacion y manda un AssertionError cuando no se cumple el “statement”
raise Exception() levanta un error creado por nosotros mismo
'''
# anejo de exepciones

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')






def my_divide(a, b):
   # Escribe tu solución 👇
   try:
      result = a / b
      return result
   except ZeroDivisionError:
      return 'No se puede dividir por 0'
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0

#ejercios practicos

'''
Ejercicio 1: Divide entre cero
Escribe un programa que solicite al usuario dos números y luego intente dividir el primer número por el segundo número. Maneja la excepción de división por cero y muestra un mensaje apropiado al usuario.
'''

try:
  num1=int(input('digite numero: '))
  num2=int(input('digite numero: '))
  result=num1/num2
  print(f'el resultado es: {result}')

except ZeroDivisionError:
    print("Invalid")
except ValueError:
    print("Error: Asegúrate de ingresar números válidos.")


'''
Ejercicio 2: Índice fuera de rango
Escribe un programa que tenga una lista de números y solicite al usuario que ingrese un índice. Luego, intenta imprimir el valor en el índice proporcionado. Maneja la excepción de índice fuera de rango y muestra un mensaje apropiado.
'''
try:
    lista_numero = [1,2,3,4,5,6,7,8,9]
    indice=int(input('Indice: '))
    print(f'El valor en el indice {indice} es: {lista_numero[indice]}')
    print(lista_numero)
except IndexError:
    print("Error: El índice ingresado es fuera de rango.")
except ValueError:
    print("Error: Asegúrate de ingresar números válidos.")

'''
Ejercicio 3: Archivo no encontrado
Escribe un programa que solicite al usuario el nombre de un archivo y luego intente abrirlo en modo lectura. Maneja la excepción de archivo no encontrado y muestra un mensaje apropiado.
'''
nombre_archivo = input("Ingresa el nombre del archivo: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo", nombre_archivo, "no se encontró.")
 

