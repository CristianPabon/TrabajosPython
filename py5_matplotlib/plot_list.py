import matplotlib.pyplot as plt

A = []
a = int(input('Número:'))
A.append(a)

while a != 1:
  if (a%2==0):
    a = a/2
    A.append(a)
  else:
    a = (a*3)+1
    A.append(a)

    continue;


print (A)

plt.plot(A)
plt.show()