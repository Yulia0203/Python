# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

from random import Random, randint
N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N+1))
print(numbers)

n = 2
print(numbers[-n:] + numbers[:-n])
