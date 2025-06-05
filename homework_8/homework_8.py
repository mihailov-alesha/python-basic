# Имена файлов
input_filename = "original.txt"
output_filename = "reversed.txt"

# 1. Чтение исходного файла как последовательности символов
with open(input_filename, "r", encoding="utf-8") as file:
    content = file.read()

# 2. Создание нового файла с обратным порядком символов
reversed_content = content[::-1]  # Переворачиваем всю строку

with open(output_filename, "w", encoding="utf-8") as file:
    file.write(reversed_content)

# 3. Вывод обоих файлов
print("Исходный файл:")
print(content)

print("\nФайл в обратном порядке:")
print(reversed_content)
