# Задание 3 Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072


def sum_numbers(num):
    numbers = int(input("Введите целое число n = "))
    sum_ = float(0)
    for i in range(1, numbers + 1):
        sum_ = sum_ + (1 + 1 / i)**i
    print(round(sum_, 3))


sum_numbers(5)

