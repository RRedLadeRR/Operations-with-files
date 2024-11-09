#Timofey

import os
def print_docs(directory):
    if not os.path.exists(directory):
        print("Директорія не існує.")
        return
    for root, dirs, files in os.walk(directory):
        print(f"Каталог: {root}")

        for dir_name in dirs:
            print(f"  Підкаталог: {dir_name}")
        for file_name in files:
            print(f"  Файл: {file_name}")
        print()

directory_path = "C:\Windows\System32"
print_docs(directory_path)