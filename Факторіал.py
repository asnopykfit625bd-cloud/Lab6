n = int(input("Введіть число для обчислення факторіала: "))

if n < 0:
    print("Факторіал для від’ємних чисел не існує!")
elif n == 0:
    print("Факторіал числа 0 = 1")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print("Факторіал числа", n, "=", factorial)