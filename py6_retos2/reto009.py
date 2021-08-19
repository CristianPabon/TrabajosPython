a = int(input('Primer número a listar:'))
b = int(input('Máximo número a listar:'))

c = 0
for x in range(a, b):
  if x%2 == 0:
    c += x  
    print(x)
print("La suma total es: ",c)