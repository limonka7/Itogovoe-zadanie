import os
import random

# Очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для ввода числа
def input_number():
    while True:
        try:
            num = int(input("Пожалуйста, введите трёхзначное число: "))
            if 100 <= num <= 999:
                return num
            else:
                print("Пожалуйста, введите трёхзначное число!")
        except ValueError:
            print("Пожалуйста, введите число!")

# Выбор режима игры
def choose_game_mode():
    while True:
        print("Выберите режим игры:")
        print("1. Играть с другим игроком (введите 1)")
        print("2. Играть с компьютером (введите 2)")
        choice = input("Ваш выбор: ")
        if choice in ('1', '2'):
            return choice
        else:
            print("Пожалуйста, выберите режим 1 или 2!")

# Игра с другим игроком
def play_with_player():
    secret_num = input_number()
    clear_console()

    print("Второй игрок, попробуйте отгадать число, задуманное первым игроком")
    print("Введите вашу догадку (3 цифры) или Esc для выхода: ")

    while True:
        input_str = input()
        if input_str == "Esc":
            break

        guess = int(input_str)

        # Проверка догадки второго игрока
        num_correct, num_in_place, temp = 0, 0, secret_num
        for _ in range(3):
            guess_digit = guess % 10
            guess //= 10
            secret_digit = temp % 10
            temp //= 10
            if guess_digit == secret_digit:
                num_in_place += 1
            elif str(secret_num).find(str(guess_digit)) != -1:
                num_correct += 1

        # Вывод результатов
        if num_in_place == 3:
            print("*** УГАДАЛИ! ***")
            break
        else:
            print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")
            print("Введите вашу догадку (3 цифры) или Esc для выхода: ")

# Игра с компьютером
def play_with_computer():
    secret_num = random.randint(100, 999)
    clear_console()

    print("Компьютер загадал число. Попробуйте отгадать его!")
    print("Введите вашу догадку (3 цифры) или Esc для выхода: ")

    while True:
        input_str = input()
        if input_str == "Esc":
            break

        guess = int(input_str)

        # Проверка догадки игрока
        num_correct, num_in_place, temp = 0, 0, secret_num
        for _ in range(3):
            guess_digit = guess % 10
            guess //= 10
            secret_digit = temp % 10
            temp //= 10
            if guess_digit == secret_digit:
                num_in_place += 1
            elif str(secret_num).find(str(guess_digit)) != -1:
                num_correct += 1

        # Вывод результатов
        if num_in_place == 3:
            print("*** УГАДАЛИ! ***")
            break
        else:
            print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")
            print("Введите вашу догадку (3 цифры) или Esc для выхода: ")

# Основная часть программы
clear_console()
mode = choose_game_mode()

if mode == '1':
    play_with_player()
elif mode == '2':
    play_with_computer()
