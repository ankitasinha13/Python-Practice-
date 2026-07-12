word = input("Enter a string:")
count = 0
for ch in word.lower():
    if ch.isalpha() and ch in "aeiou":
        count += 1
print("No of vowel:",count)
