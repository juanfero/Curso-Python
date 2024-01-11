def my_function():
    print("Hello from a function")
my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# si no sé  cuantos argumentos voy a meter reaizo lo siguiente.
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''
def funcion(text):
    print(text*2)
funcion('pipe')


def suma(a,b):
    funcion(a*2)
    funcion(b*2)
suma(4,6)


def nombre(name):
    print(f'juan {name}')
nombre('felipe')

'''

'''
def sumatoria(num_1,num_2):
    plus=0
    for i in range(num_1,num_2):
        plus+=i
    return plus         

result=sumatoria(1,11)
print(result)
result_2=sumatoria(result,70)
print(result_2)

'''

'''
def my_function(x):
    return(5 * x) 

my_function(10)
print(my_function(3))
print(my_function(5))
print(my_function(9))
'''

def funcion1(x):
    return x * 2

def funcion2(y):
    return y + 5

def funcion_compuesta(z):
    resultado1 = funcion1(z)
    resultado2 = funcion2(z)
    return resultado1, resultado2

resultado = funcion_compuesta(3)
print(resultado)  # Esto imprimirá una tupla con los resultados de ambas funciones: (6, 8)

def plus(x):
    return x*2
eso=plus(5)
print(f'siuu {eso}')

def suma(y):
    return plus(y+2)
sii=suma(4)
print(sii)

def factorial (n):
    if n ==0:
        return 1
    else:
        return n * factorial(n -1)
    
resultad=factorial(5)
print(f'el resultado es {resultad}')


def plus(x):
    return x*2

def suma(y):
    return plus(y+2)

def solucion (k):
    esoo=plus(k+5)
    sip=suma(k+7)
    return esoo, sip
se=solucion(4)
print(set(se))

def ordenar(listas):
    return listas.sort()
prueba=[1,4,2,8,2,18]
ordenar(prueba)
print(prueba)

def eliminar(listas):
    return listas.remove(4)
eliminar(prueba)
print(prueba)


def agregar(esoo):
    return esoo.extend([1,5,246,32,2])
se=[]
agregar(se)
print(se)

def suma (a,b):
    return (a+b)
solution=suma(2,4)
print(solution)

def maximo(lista):
    return max(lista)
numeros=[1,42,2,6,32]
solution_1=maximo(numeros)

print(solution_1)

def ordenar(listas):
    return listas.sort()
prueba=[1,4,2,8,2,18,2]
ordenar(prueba)
print(prueba)

def lord(lista):
    new=sorted(lista)
    return new
w=[1,8,4,6,2]
print(lord(w))

def reverso (texto):
    return texto[::-1]
siuu=reverso('pipe')
print(siuu)

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n -1)
si=factorial(5)
print(si)

def conteo(lista,elemento):
    return lista.count(elemento)
sk=conteo(prueba,2)
print(sk)

def primo(numero):
    if numero %2==0:
        print('par')
    else:
        print('impar')
numero=5
primo(numero)

def potencia(base,exponente):
    return base**exponente
print(potencia(3,5))


def suma(a,f):
    return a+f

def resta(a,f):
    return a-f

def multiply(a,f):
    return a*f

def split(a,f):
    if f != 0:
        return a/f
    else:
        print('error splitting')


def calculate(a,f):
    sumar = suma(a,f)
    restar = resta(a,f)
    multiplicar = multiply(a,f)
    dividir = split(a,f)
    return sumar, restar,multiplicar, dividir

epa = calculate(2,6)
print(epa)