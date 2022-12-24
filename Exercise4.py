# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = 46
def binary_num(num):
    my_list = []
    while num > 0:
        my_list.append(str(num % 2))
        num = int(num / 2)
    m = ""
    for i in range(len(my_list)):
        m += my_list[len(my_list) - 1 - i]
    return m

print(f"десятичное число {n}, двоичное число {binary_num(n)}")