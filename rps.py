import random

print("Это игра Камень-ножницы-бумага. Попробуй победи компьютер")
variants = ["камень", "ножницы", "бумага"]

comp = random.choice(variants)
player = input(f"Введи, что будешь ставить ({variants}):")
print(f"Компьютер выбрал вариант {comp}")

player_win = False
comp_win = False

if player == "ножницы" and comp == "бумага":
    player_win = True
elif player == "ножницы" and comp == "камень":
    comp_win = True
elif player == "ножницы" and comp == "ножницы":
    pass

elif player == "бумага" and comp == "бумага":
    pass   
elif player == "бумага" and comp == "камень":
    player_win = True
elif player == "бумага" and comp == "ножницы":
    comp_win = True

elif player == "камень" and comp == "бумага":
    comp_win = True
elif player == "камень" and comp == "камень":
    pass
elif player == "камень" and comp == "ножницы":
    player_win = True

if player_win:
    print("Вы победили")
elif comp_win:
    print("Компьютер победил!")
else:
    print("Ничья!")
