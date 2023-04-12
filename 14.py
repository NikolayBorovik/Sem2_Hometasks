# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k
# ), не превосходящие числа N.

n = int(input('Enter your number: '))
print(1, end=" ")
for i in range(1, n//2+1):
    result = 2*i
    print(result, end=' ')    