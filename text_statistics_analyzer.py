text = input("Enter a string: ")

vowels = 0
consonanats = 0
digits = 0
spaces = 0

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonanats += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Text statistics:")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonanats}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")