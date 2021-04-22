for i in range(1,11):
  for j in range(1,11):
    print ('%d * %d = %d' % (i,j,i*j))
    if j == 10:
      print("_"*40)