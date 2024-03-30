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

# Ввод имён игроков
def input_player_names():
    while True:
        try:
            num_players = int(input("Введите количество игроков (от 2 до 10): "))
            if 2 <= num_players <= 10:
                names = []
                for i in range(num_players):
                    name = input(f"Введите имя игрока {i + 1}: ")
                    names.append(name)
                return names
            else:
                print("Пожалуйста, введите число от 2 до 10!")
        except ValueError:
            print("Пожалуйста, введите число!")

# Игра с другим игроком
def play_with_player(secret_num, players):
    attempts = 0
    while True:
        for player in players:
            attempts += 1
            print(f"\nХод игрока {player}:")
            guess = input_number()
            clear_console()

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
                print(f"Введите вашу догадку, игрок {player} (3 цифры): ")

# Игра с компьютером
def play_with_computer(secret_num):
    attempts = 0
    while True:
        attempts += 1
        guess = random.randint(100, 999)
        clear_console()

        # Проверка догадки компьютера
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
            print(f"*** Компьютер угадал число с {attempts} попытки! ***")
            return
        else:
            print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")
            print("Компьютер делает догадку...")
            input("Нажмите Enter для продолжения...")

# Основная часть программы
clear_console()
mode = choose_game_mode()
if mode == '1':
    players = input_player_names()
    secret_num = input_number()
    play_with_player(secret_num, players)
elif mode == '2':
    secret_num = random.randint(100, 999)
    play_with_computer(secret_num)
