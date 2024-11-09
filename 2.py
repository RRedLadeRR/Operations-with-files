#Timofey

with open("numbers.txt", "r") as file:
    numbers = [float(line.strip()) for line in file]

total_sum = sum(numbers)
max_value = max(numbers)

with open("numbers.txt", "a") as file:
    file.write(f"\nСума: {total_sum}\n")
    file.write(f"Максимум: {max_value}\n")

print("Сума і максимум дописані у файл numbers.txt")