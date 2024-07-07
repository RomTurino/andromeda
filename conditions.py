expression = 2 + 2 == 4
print(expression)
print(type(expression))
if expression:
    print("Математика жива!")


is_five_greater_than_two = 5 >= 2
is_ten_equal_to_five = 10 == 5
is_three_not_equal_to_four = 3 != 4
print(is_five_greater_than_two)  # True
print(is_ten_equal_to_five)      # False
print(is_three_not_equal_to_four) # True
if is_five_greater_than_two:
    print('5 больше, чем 2')

if is_ten_equal_to_five:
    print('10 равно 5')

if is_three_not_equal_to_four:
    print('3 не равно 4')
