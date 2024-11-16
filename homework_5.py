import random
secret_number = random.randint(1, 50)
guesses_made = 5

print("Игра попробуй угадать число! Я загадываю а ты угадываешь.")

while True:
    assumption = int(input("Введите ваше предполагаемое число. От 1 до 50: "))

    guesses_made -= 1

    if assumption < secret_number:
        print("Загаданное число больше.")
    elif assumption > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Вы угадали число: {secret_number}!")
        print(f"Число попыток: {guesses_made}")
        break

