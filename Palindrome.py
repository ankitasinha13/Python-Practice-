word = input("Enter a string:")
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
    
if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")
