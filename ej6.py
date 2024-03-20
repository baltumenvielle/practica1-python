my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []

for i in range(len(my_list)):
  if (my_list[i] % 2 == 0):
    even_list.append(my_list[i])
  else:
    odd_list.append(my_list[i])

for i in range(len(even_list)):
  print(even_list[i])
for i in range(len(odd_list)):
  print(odd_list[i])