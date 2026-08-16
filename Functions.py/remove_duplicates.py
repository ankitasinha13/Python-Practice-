def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [1, 2, 2, 3, 4, 4, 5, 3]
result = remove_duplicates(numbers)
print("Original list:", numbers)
print("After removing duplicates:", result)
