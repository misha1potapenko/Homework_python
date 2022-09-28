# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

def create_list(num):
    numbers = int(input("Введите целое значение N = "))
    list_for = []
    start = numbers * -1
    finish = numbers * 2
    for i in range(0, finish + 1):
        list_for.append(start)
        start += 1
    print(list_for)
    position_first = int(input("Ведите первую позицию "))
    position_second = int(input("Ведите вторую позицию "))
    product = list_for[position_first + 1] * list_for[position_second + 1]
    print(product)


create_list(5)