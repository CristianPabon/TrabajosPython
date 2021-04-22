año =2012 #Año a investigar

if (año%4==0 and (not(año%400==0) or año%100==0)):
  print("es una año bisiesto") 
else:
  print("no es bisiesto")