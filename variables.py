# print("2" + "2")
# print("Все мужчины думают про Римскую империю")
# print("Все мужчины думают про Римскую империю")
# print('И воскликнул Цезарь: "И ты, Брут!"')
# print("Bruce " + "Wayne")  # конкатенация

# print(type(245))
# print(type("bruce"))
# print(type(print))

# name = input("Enter your name:  ") # отдает нам строку
# city = input("Enter your city: ")
# print("hello, " + name + " from " + city)
# print(type(name))

glass_1 = "Baikal"
glass_2 = "Dushes"
glass_3 = glass_1
print("Перелили из первого стакана в третий лимонад " + glass_3)
glass_1 = glass_2
print("Перелили из второго стакана в первый лимонад " + glass_1)
glass_2 = glass_3
print("Перелили из третьего стакана во второй лимонад " + glass_2)

print(glass_1, glass_2)
glass_1, glass_2 = glass_2, glass_1
print(glass_1, glass_2)


money = 1000
notebook = 150
pen = 50
chocolate = 120

money = money - notebook - pen - chocolate

print("У вас осталось " + str(money) + " рублей")


current_money = 2000
game_price = 2400
difference = game_price - current_money
print(f"Вам не хватает " + str(difference) + " рублей")


budget = 1500
ticket_price = 350

tickets = budget // ticket_price
remaining_money = budget % ticket_price
print(f"Вы можете купить " + str(tickets) + " билетa")
print(f"У вас останется " + str(remaining_money) + " рублей")

number = int(input("Введите трехзначное число: "))
last_digit = number % 10
first_digit = number // 100
middle_digit = number // 10 % 10
print(first_digit, middle_digit, last_digit)
sum_digits = first_digit + middle_digit + last_digit
print(f"Сумма цифр в числе {number} = {sum_digits}")
