# while = повторять пока

# number = 1
# while number <= 5:
#     print(number)
#     number += 1
# import time

# number = 100
# factorial = 1
# summa = 0
# while number > 0:
#     # time.sleep(1)
#     summa += number
#     factorial *= number
#     print(f"Число {number} прибавлено. Сумма = {summa}, факториал = {factorial}")
#     number -= 1

# counter = 20

# while counter <= 60:
#     print(counter)
#     counter += 10

rain = True
while rain:
    print("Я сижу дома")
    stop = input("Дождь закончился? ")
    if stop == "да":
        print("Я выхожу из дома")
        break
