def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


numbers = [10, 5, 8, 20, 15]

result = find_second_largest(numbers)

print("Second largest number:", result)
