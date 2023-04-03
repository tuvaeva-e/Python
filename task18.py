"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел A. Последняя строка
содержит число X"""

n = int(input('Введите число элементов массива: '))
print('Введите элементы массива: ')
array = [int(input()) for _ in range(n)]
x = int(input('Введите число X: '))

result = array[0]
result_list = list()
result_list.append(str(result))  
min_difference = abs(x - array[0])

for number in array[1:]:
    if abs(number - x) < min_difference:
        result = number
        min_difference = abs(number - x)
        result_list.clear()
        result_list.append(str(result))
    elif abs(number - x) == min_difference:
        result_list.append(str(number))

print(f'К {x} наиболее близко число: {", ".join(set(result_list))}.')
