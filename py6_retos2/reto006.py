import random
x=random.randrange(121)
if x < 10:
  print('El número', x, 'es menor de 10')
elif x >= 10 & x < 50:
  print('El número', x, 'se encuentra entre 10 y 50')
elif x >= 50 & x < 100:
  print('El número', x, 'se encuentra entre 50 y 100')
elif x >= 100:
  print('El número', x, 'es mayor de 100')

