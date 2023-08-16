numbers = [2, 2, 4, 5, 3, 3, 4, 1, 4, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)