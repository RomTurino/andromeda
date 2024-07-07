import random

is_left = False
print("Вы находитесь в древнем лесу, где спрятаны сокровища. Вам нужно выбрать путь.")
answer = input("Введите 'лево', 'право' или 'прямо': ").lower()
if answer == "лево":
    is_left = True
    
elif answer == "право":
    print("Вы нашли безопасное место для отдыха. Но здесь нет сокровищ.")
elif answer == "прямо":
    print("Вы встретили мудрого старца, который дал вам карту к сокровищам!")
else:
    print("Вы заблудились. Попробуйте снова.")
    
if is_left:
    opportunity = random.randint(1,3)
    if opportunity == 1:
        print("Поздравляем! Вы нашли сокровище!")
    elif opportunity == 2:
        print("Вы ничего не нашли. Попробуйте снова.")
    else:
        print("О нет! Вы попали в ловушку!")