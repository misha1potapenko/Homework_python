
# первая задача
n = int(input("Введите число "))
list = range(n)
print(f"{n}:", end=" ")
for i in list:
    i = randint(-100,100)
    print(i, end=" ")

# вторая задача
n = int(input("Введите число "))
n = abs(n)
list = range(1,n+1)
print(f"n = {n}:", end=" ")
for n in list:
    n = 3*n + 1
    print(n, end=" ")

# вторая задача
lst1 = [1, 2, 9, 4, 12, 6]
lst2 = [2, 1, 9, 12, 6, 4]
count = 0
for i in lst1:
    for j in lst2:
        if i==j:
            count=count+1
print(f"{lst1}\n{lst2}")
print (count)

count = 0
k = 1
for i in range(0,len(str1) - len(str2),k):
    if str2 in str1[i:i+len(str2)]:
        count += 1
        k = len(str2)
    else:
        k = 1
print(f"Вторая строка входит в первую {count} раз(а).")
