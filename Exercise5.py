# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


my_list = [-1, -1, 0, 1, 1]
num = int(input("Введите число: "))

fib1 = fib2 = 1
 
for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    my_list.append(fib2)

fib1 = fib2 = -1

for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    my_list.insert(0, fib2)

print(my_list)