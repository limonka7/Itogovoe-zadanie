import os

# Очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Первый игрок задумывает число
clear_console()
secret_num = int(input("Первый игрок, пожалуйста, введите тайное число (3 цифры): "))

# Очистка консоли
clear_console()

# Игра начинается
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
