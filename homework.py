# Решение задачи №1.
total_money = 3000
book_price = 450
books = total_money // book_price
remaining = total_money % book_price
print(f'Вы можете купить {books} книг и у вас останется {remaining} рублей')
# Решение задачи №2.
grade1 = 4
grade2 = 5
grade3 = 3
grade4 = 4
grade5 = 5
average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
print(f'Ваша средняя оценка: {average_grade}')
# Решение задачи №3.
total_money = 5000
stock_price = 134.65
num_stocks = total_money // stock_price
remaining_money = total_money % stock_price
print(f'Ваня сможет купить {num_stocks} акций')
print(f'У Вани останется {round(remaining_money, 2)} рублей')
