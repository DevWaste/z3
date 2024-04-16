word = input("Введите слово из маленьких латинских букв: ")

# Гласные и счетчики
vowels = "aeiou"
vowel_counts = {v: 0 for v in vowels}

# Подсчет гласных и согласных
for letter in word:
    if letter in vowels:
        vowel_counts[letter] += 1

# Вывод результатов
total_vowels = sum(vowel_counts.values())
total_consonants = len(word) - total_vowels
print(f"Гласных букв: {total_vowels}, согласных букв: {total_consonants}")

for vowel in vowels:
    if vowel_counts[vowel] == 0:
        print(vowel, False)
    else:
        print(vowel, vowel_counts[vowel])
