import random

number = random.randint(1, 100)
attempts = 7
count = 0

print("Я загадав число від 1 до 100. Спробуй вгадати!")

while count < attempts:
    guess = int(input(f"Спроба {count + 1}/{attempts}: "))
    count += 1

    if guess == number:
        print("🎉 Вітаю! Ти вгадала число!")
        break
    elif guess < number:
        print("Більше!")
    else:
        print("Менше!")

if count == attempts and guess != number:
    print(f"❌ Спроби закінчились. Було загадано: {number}")
