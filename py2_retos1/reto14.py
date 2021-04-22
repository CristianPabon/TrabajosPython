num=-10
def resp(num):
  resultado=[]
  while num<11:
    resultado.append(num**2)
    num+=1
  return(resultado)
def ed():
  print('Programa finalizado')
print(resp(num))
ed()