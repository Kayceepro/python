numbers = [ 2, 3 ,6, 7, 2, 9 ]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)