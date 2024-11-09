#Timofey

import os
import shutil

def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Файли у папці '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Папка '{directory}' не знайдена.")
    except PermissionError:
        print(f"У вас немає прав для доступу до папки '{directory}'.")

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Файл '{src}' успішно скопійовано в '{dst}'.")
    except FileNotFoundError:
        print(f"Файл '{src}' не знайдений.")
    except PermissionError:
        print(f"У вас немає прав для копіювання файлу.")
    except Exception as e:
        print(f"Помилка при копіюванні файлу: {e}")

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print(f"Файл '{src}' успішно переміщено в '{dst}'.")
    except FileNotFoundError:
        print(f"Файл '{src}' не знайдений.")
    except PermissionError:
        print(f"У вас немає прав для переміщення файлу.")
    except Exception as e:
        print(f"Помилка при переміщенні файлу: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файл '{file_path}' успішно видалено.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдений.")
    except PermissionError:
        print(f"У вас немає прав для видалення файлу.")
    except Exception as e:
        print(f"Помилка при видаленні файлу: {e}")

def main():
    directory = input("Введіть шлях до папки: ")
    
    list_files(directory)
    
    while True:
        print("\nОберіть операцію:")
        print("1. Копіювати файл")
        print("2. Перемістити файл")
        print("3. Видалити файл")
        print("4. Вийти")
        
        choice = input("Ваш вибір (1/2/3/4): ")
        
        if choice == '1':
            src = input("Введіть шлях до файлу для копіювання: ")
            dst = input("Введіть шлях до папки, куди скопіювати: ")
            copy_file(src, dst)
        
        elif choice == '2':
            src = input("Введіть шлях до файлу для переміщення: ")
            dst = input("Введіть шлях до папки, куди перемістити: ")
            move_file(src, dst)
        
        elif choice == '3':
            file_path = input("Введіть шлях до файлу для видалення: ")
            delete_file(file_path)
        
        elif choice == '4':
            print("Вихід з програми.")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()