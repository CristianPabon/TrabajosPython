altura=1.79 #Altura a a tener en cuenta
peso=76 #Peso a tener en cuenta

print('Su peso es', peso, 'y su altura es', altura)

resultado= peso/(altura**2)

print('Su IMC es de ', resultado)

if (resultado<16):
  print('Desnutrición')
elif (resultado<20):
  print('Bajo peso')
elif (resultado<24):
  print('Normal')
elif (resultado<29):
  print('Sobre peso')
elif (resultado<34):
  print('Obesidad')
elif (resultado<39):
  print('Obesidad marcada')
elif (resultado>40):
  print('Obesidad morbida')
else:
  print('No encontrado')
