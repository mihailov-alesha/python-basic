# вариант 1 с обходом диапазона чисел в цикле
total = 0
for number in range(2, 101, 2):
    total += number
print(f'вариант 1: {total}')

# вариант 2 с генератором списка
total = sum([x for x in range(2, 101, 2)])
print(f'вариант 2: {total}')

# вариант 3 с функцией sum() и range() без цикла
total = sum(range(2, 101, 2))
print(f'вариант 3: {total}')
