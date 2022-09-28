# Задание 5 Реализуйте алгоритм перемешивания списка.

import random

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(1, 10))
print(rand_list)


def shake_list(rand_list):
    for i in range(0, 10):
        rand_list[i] = rand_list[random.randrange(1, 10)]
    print(rand_list)


shake_list(rand_list)

