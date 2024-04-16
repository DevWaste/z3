number = int(input("Введите целое число: "))

# Определение типа числа и его четности
if number == 0:
    description = "нулевое число"
elif number > 0:
    if number % 2 == 0:
        description = "положительное четное число"
    else:
        description = "положительное нечетное число"
else:
    if number % 2 == 0:
        description = "отрицательное четное число"
    else:
        description = "отрицательное нечетное число"

print(description)
if number % 2 != 0:
    print("число не является четным")
