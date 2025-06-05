original_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Вариант 1 - используем генератор словаря для фильтрации
new_dict = {key: value for key, value in original_dict.items() if value >= 3}
print(new_dict)

# Вариант 2 - используем функцию filter() и лямбда-функцию
new_dict = dict(filter(lambda item: item[1] >= 3, original_dict.items()))
print(new_dict)
