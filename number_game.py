import random
import math

print('Это игра "Угадай число"')

min_num = ""
while not min_num.isdigit():
    min_num = input("Введите минимальное число, которое я могу загадать: ")
min_num = int(min_num)

max_num = ""
while not max_num.isdigit():
    max_num = input("Введите максимальное число, которое я могу загадать: ")
max_num = int(max_num)

tries = math.log(max_num - min_num)
tries = math.ceil(tries)
print(f"Компьютер загадал число от {min_num} до {max_num}. Попробуй его угадать за {tries} попыток")
secret_number = random.randint(min_num, max_num)
while tries > 0:
    print(f"Количество оставшихся попыток: {tries}")
    user_number = input("Введи число: ")
    if not user_number.isdigit():
        print("Вы ввели не число")
        continue
    tries -= 1
    user_number = int(user_number)
    if user_number == secret_number:
        print("Вы угадали мое число!")
        break
    elif user_number > secret_number:
        print("Ваше число больше моего")
    elif user_number < secret_number:
        print("Ваше число меньше моего")
    