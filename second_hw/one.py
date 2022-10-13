# 14.	Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# o	6782 -> 23
# o	0,56 -> 11




def sum_number(num):
    number = input("Введите число: ")
    string_number = str(number)
    count = len(string_number)
    print(string_number)
    list = []
    for i in range(0, count):
        list.append(string_number[i])
    if "." in list:
        list.remove(".")
    if "-" in list:
        list.remove("-")
    print(list)
    sum_num = 0
    for i in list:
        sum_num = sum_num + int(i)
    return sum_num
    # print(f'Сумма чисел равна {sum_num}')


sum_ = (sum_number(5))
print(f'Сумма чисел равна {sum_}')
