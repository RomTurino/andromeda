import random

bank_account = 0
lottery_number = random.randint(1, 5)
user_number = int(input("Введите число от 1 до 5 для участия в лотерее: "))

if lottery_number == user_number:
    print("Вы угадали!")
    bank_account += 1500
    print(f"На вашем счету теперь {bank_account} рублей")
else:
    print(f"Загаданное число: {lottery_number}")
    print(f"Ваше число: {user_number}")