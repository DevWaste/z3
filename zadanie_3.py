A = int(input("Сколько долларов у Майкла? "))
B = int(input("Сколько долларов у Ивана? "))
X = int(input("Минимальная сумма инвестиций? "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)
