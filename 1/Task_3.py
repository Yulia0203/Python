# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

x = int(input('Enter X: '))
y = int(input('Enter Y: '))

if x > 0 and y > 0:
    print('1')
elif x < 0 < y:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif y < 0 < x:
    print('4')
else:
    print('Error, 0 entered!')