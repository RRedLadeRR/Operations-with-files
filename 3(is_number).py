#Timofey

def is_number(value):
    if value.isnumeric():
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if is_number(line):
            numbers.append(float(line))

if numbers:
    total_sum = sum(numbers)
    max_value = max(numbers)
else:
    total_sum = 0
    max_value = None

with open("numbers.txt", "a") as file:
    file.write(f"\nСума: {total_sum}\n")
    if max_value is not None:
        file.write(f"Максимум: {max_value}\n")
    else:
        file.write("Максимум: відсутнє дійсне значення\n")

print("Сума і максимум (якщо є) дописані у файл numbers.txt")