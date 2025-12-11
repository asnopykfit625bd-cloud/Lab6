height = int(input("Введіть висоту ялинки: "))

for i in range(1, height + 1):
    stars = "*" * (2*i - 1)
    spaces = " " * (height - i)
    print(spaces + stars)
