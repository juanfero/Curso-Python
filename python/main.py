from scripts.modulo1 import run
from scripts.modulo2 import cor

print(run(4))
print(cor(2))


#otra forma de importar.(la mejor forma de llamar)

import scripts
print(scripts.modulo1.run)

'''
Para acceder a los módulos de los paquetes podemos utilizar estas opciones:
import nombrecarpeta.nombremodulo
from nombrecarpeta import nombremodulo
from nombrecarpeta.nombremodulo import def
'''

from scripts import modulo1 
print(scripts.sumar(5,7))
print(scripts.restar(5,7))



import scripts.modulo1
print(scripts.modulo1.sumar(5,7))
print(scripts.modulo1.restar(5,7))