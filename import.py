import modulo
print(modulo.name)
modulo.square(10)
modulo.rectangle(2.3,4.5)
#alias (rename the file)
import modulo as m
print(m.name)
print(m.square(10))
print(m.rectangle(2.3,7.5))
from modulo import *
print(name)
square(10)
rectangle(2.3,4.5)
from modulo import square
print(square(11))

