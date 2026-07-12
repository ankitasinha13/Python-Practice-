word = input("Enter a string:")
count = 0
for ch in word.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("No of consonants:",count)
