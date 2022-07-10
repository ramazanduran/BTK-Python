"""
Okunakta fayda var.
https://medium.com/kodelim/mod%C3%BCller-220e7390e517
https://python-istihza.yazbel.com/moduller.html
"""

# Yöntem 1
"""
import math
import math as islem

value = dir(math)
value = help(math)
value = help(math.factorial)
value = math.sqrt(49)
value = math.factorial(5)
value = math.floor(5.9)
value = math.ceil(5.9)

value = islem.factorial(5)
"""
# Yöntem 2
#from math import *  #(burada * bütün özelliklerini çalştır demek)

def sqrt(x):
    print('x :'+ str(x))

from math import factorial,sqrt,ceil

# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)