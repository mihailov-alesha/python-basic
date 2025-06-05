numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

# вариант 1 - фильтрация лямбда-функцией
# Фильтруем числа: оставляем нечётные (x % 2 != 0) и большие 50
filtered_numbers = filter(lambda x: x % 2 != 0 and x > 50, numbers)

# Преобразуем результат в список и выводим
print(list(filtered_numbers))

# вариант 2 - фильтрация обычной функцией
def is_odd_and_gt_50(x):
    return x % 2 != 0 and x > 50

# Преобразуем результат в список и выводим
print(list(filter(is_odd_and_gt_50, numbers)))
