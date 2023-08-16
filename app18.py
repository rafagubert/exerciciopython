def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [1, 5, 2, 77, 3]
print("The highest number is:", find_max(numbers))

