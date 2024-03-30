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
            if len(names) < 1:
                print("Должен быть как минимум один игрок!")
            else:
                clear_console()
                return names
        else:
            names.append(name)

# Функция для отображения меню выбора режима игры
def show_game_menu():
    clear_console()
    mode = input("Выберите режим игры:\n1. Игра с другими игроками\n2. Игра с компьютером\n3. Выйти из игры\nВаш выбор: ")
    if mode == '1':
        players = input_player_names()
        clear_console()
        play_with_players(players)
    elif mode == '2':
        players = input_player_names()
        clear_console()
        play_with_computer(players)
    elif mode == '3':
        exit()

# Игра с другими игроками
def play_with_players(players):
    clear_console()
    secret_num = input_number("Пожалуйста, введите секретное трёхзначное число: ")
    clear_console()
    attempts = 0
    current_player = 0
    while True:
        attempts += 1
        player = players[current_player]
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
            input("Нажмите Enter для продолжения...")
            show_game_menu()
            break
        else:
            print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")

        # Переключение на следующего игрока
        current_player = (current_player + 1) % len(players)

# Игра с компьютером
def play_with_computer(players):
    clear_console()
    secret_num = random.randint(100, 999)
    current_player = 0
    for _ in range(len(players)):
        attempts = 0
        while True:
            attempts += 1
            player = players[current_player]
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
                input("Нажмите Enter для продолжения...")
                show_game_menu()
                return
            else:
                print(f"Угадано: {num_correct + num_in_place} На своих местах: {num_in_place}")

            # Переключение на следующего игрока
            current_player = (current_player + 1) % len(players)

# Основная часть программы
clear_console()
show_game_menu()
