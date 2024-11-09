#Timofey

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"

with open("poem.txt", "r", encoding="utf-8") as file:
    poem = file.read()

print("Текст вірша:")
print(poem)

words = poem.split()

vowel_start_count = 0
consonant_start_count = 0

for word in words:
    word = word.strip(".,!?-\"'")
    if word:
        first_letter = word[0].lower()
        if first_letter in vowels:
            vowel_start_count += 1
        else:
            consonant_start_count += 1

print("\nРезультати підрахунку:")
print(f"Слів, що починаються на голосну: {vowel_start_count}")
print(f"Слів, що починаються на приголосну: {consonant_start_count}")

if vowel_start_count > consonant_start_count:
    print("У вірші більше слів, що починаються на голосну літеру.")
elif consonant_start_count > vowel_start_count:
    print("У вірші більше слів, що починаються на приголосну літеру.")
else:
    print("Кількість слів, що починаються на голосну і приголосну літери, однакова.")