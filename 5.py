#Timofey

with open("seating.txt", "r") as file:
    hall = [list(map(int, line.split())) for line in file]

with open("seating.txt", "r", encoding="utf-8") as file:
    seating = file.read()

print("Місця:")
print(seating)

free_seats = sum(row.count(0) for row in hall)
print(f"Кількість вільних місць у залі: {free_seats}")

row_num = int(input("Введіть номер ряду: ")) - 1
seat_num = int(input("Введіть номер місця: ")) - 1

if 0 <= row_num < len(hall) and 0 <= seat_num < len(hall[row_num]):
    if hall[row_num][seat_num] == 0:
        print("Місце вільне.")
    else:
        print("Місце зайняте.")
else:
    print("Некоректний номер ряду або місця.")