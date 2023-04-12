# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

coins = int(input('Enter total number of coins: '))
heads = 0
trails = 0
for i in range(coins):
    side = input(f'Enter side of the coin{i+1} (head or trail): ')
    if side == 'trail':
        trails +=1
    elif side == 'head':
        heads += 1
if trails<heads:
    print(f"Turn trails upside down {trails} times")
else:
    print(f"Turn heads upside down {heads} times")