# Завдання: 
# Створіть список чисел. 
# Подвойте кожне число у списку та виведіть результат.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = []

for number in numbers:
    new_numbers.append(number * 2)

print(new_numbers)