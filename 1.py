#Timofey

numbers = input("Введіть числа через пробіл: ")
numbers_list = numbers.split()

with open("numbers.txt", "w") as file:
    for number in numbers_list:
        file.write(number + "\n")

print("Числа записані у файл numbers.txt")