my_list = []

num = int(input('Ingrese un numero '))
while (num != 0):
  my_list.append(num)
  num = int(input('Ingrese un numero '))
  
for i in range(len(my_list)):
  if (my_list[i] < 0):
    break
  print(my_list[i])