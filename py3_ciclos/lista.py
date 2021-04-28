def lista(A,B):
  n = len(A)//2
  c=[]
  for i in range (n):
    h = ((A[i+1])**2)*(B[2*i])
    f = h+(B[n+1])
    c.append(f)
  return c

A=[1,2,3,9]
B=[4,5,6,7]
lista(A,B)

#Prueba
t=[((4*4)+6),((9*6)+7)]
t