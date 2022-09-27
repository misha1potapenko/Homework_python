# 8.	Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# o	x=34; y=-30 -> 4
# o	x=2; y=4-> 1
# o	x=-34; y=-30 -> 3


abscissa = float(input("Введите Х = "))
ordinates = float(input("Введите У = "))
if abscissa > 0 and ordinates > 0:
    print("Это 1 четверть")
elif abscissa > 0 and ordinates < 0:
    print("Это 4 четверть")
elif abscissa < 0 and ordinates > 0:
    print("Это 2 четверть")
elif abscissa < 0 and ordinates < 0:
    print("Это 3 четверть")
elif abscissa == 0:
    print("Точка лежит на оси х")
elif ordinates == 0:
    print("Точка лежит на оси y")
