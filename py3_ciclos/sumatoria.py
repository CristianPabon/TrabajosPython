def sumatoriaa(A,B,C):

  n = len(A)
  acumulador = 0
  for i in range (n):
    h = A[i]*B[i]
    f = h+C[i]
    acumulador = acumulador+f
    resultado = acumulador +(n**2)
  return resultado
  
A = [1,1,1,1]
B = [2,2,2,2]
C = [3,3,3,3]
sumatoriaa(A,B,C)

#Prueba
t=(((1*2)+3)+((1*2)+3)+((1*2)+3)+((1*2)+3))+(4)**2
t