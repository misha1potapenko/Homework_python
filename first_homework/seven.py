# 7.	Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("x y z f_1  f_second")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f_first = not(x or y or z)
            f_second = not(x) and not(y) and not(z)
            print(x, y, z, bool(f_first), bool(f_second))
