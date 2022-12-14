# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))


