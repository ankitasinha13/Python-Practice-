word = input("Enter a string:")
count = 0
for ch in word:
    word = ch + word
    count += 1
print("Length of a string:",count)
