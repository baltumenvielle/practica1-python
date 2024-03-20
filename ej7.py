my_list = []
my_string = ''

num = int(input('Ingrese un numero entero '))
while num != 0:
  my_list.append(num)
  num = int(input('Ingrese un numero entero '))

for i in range(len(my_list)):
  if (my_list[i] % 3 != 0):
    my_string += str(my_list[i])
    if (i != len(my_list)-1):
      my_string += '-'

print(my_string)
