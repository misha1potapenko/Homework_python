# 15.	Напишите программу, которая принимает на
# вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# o	пусть N = 4, тогда [ 1, 2, 6, 24 ]\
#     (1, 1*2, 1*2*3, 1*2*3*4)

numbers = int(input("Введите число "))
list = []
multiplication = 1
for i in range(1, numbers + 1):
    list.append(multiplication * i)
    multiplication = multiplication * i
print(list)
