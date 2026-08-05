text = input()
vowel_count = 0

for i in text:
    if i in "AEIOUaeiou":
        vowel_count += 1
print(vowel_count)