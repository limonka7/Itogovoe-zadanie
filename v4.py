import os
import random

# Очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для ввода числа
def input_number(message):
    while True:
        try:
            num = int(input(message))
            if 100 <= num <= 999:
                return num
            else:
                print("Пожалуйста, введите трёхзначное число!")
        except ValueError:
            print("Пожалуйста, введите число!")

# Ввод имён игроков
def input_player_names():
    names = []
    print("Введите имена игроков. Введите 'готово', чтобы закончить.")
    while True:
        name = input("Введите имя игрока: ")
        if name.lower() == 'готово':
            if len(names) < 2:
                print("Должно быть как минимум два игрока!")
            else:
                clear_console()
                return names
        else:
            names.append(name)

# Игра с другими игроками
def play_with_players(players):
    secret_num = input_number("Пожалуйста, игрок 1, введите секретное трёхзначное число: ")
    attempts = 0
    while True:
        for player in players:
            attempts += 1
            print(f"\nХод игрока {player}:")
            guess = input_number(f"Введите вашу догадку, игрок {player} (3 цифры): ")

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
                print(f"*** {player} угадал число с {attempts} попытки! ***")
                return
            else:
                print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")

# Игра с компьютером
def play_with_computer(players):
    secret_num = random.randint(100, 999)
    for player in players:
        attempts = 0
        while True:
            attempts += 1
            print(f"\nХод игрока {player}:")
            guess = input_number(f"Введите вашу догадку, игрок {player} (3 цифры): ")

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
                print(f"*** {player} угадал число с {attempts} попытки! ***")
                break
            else:
                print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")

# Основная часть программы
clear_console()
mode = input("Выберите режим игры:\n1. Игра с другими игроками\n2. Игра с компьютером\nВаш выбор: ")
if mode == '1':
    players = input_player_names()
    clear_console()
    play_with_players(players)
elif mode == '2':
    players = input_player_names()
    clear_console()
    play_with_computer(players)
