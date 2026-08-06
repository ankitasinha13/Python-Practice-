def is_vowel(alphabet):
    if alphabet in "aeiou":
        return (alphabet,"is vowel")
    else:
        return (alphabet,"is consonant")
check1 = is_vowel("i")
check2 = is_vowel("c")
print(check1)
print(check2)
