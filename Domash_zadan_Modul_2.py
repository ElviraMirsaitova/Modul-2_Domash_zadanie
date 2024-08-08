chislo = int(input("Введите число от 3 до 20: "))
print(chislo)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
for i in numbers:
    para = True

    for j in range(1, i):
        submatrix = []
        if chislo % (i + j) == 0:
            submatrix.append(j),submatrix.append(i)
            result.append(submatrix)
pobeda = sorted(result)
print(pobeda)

#в первый раз решила сама, никуда не заглядывая. Подкатывают слезы счастья :D