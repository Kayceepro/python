for x in range(4):
    for y in range(3):
        print(x, y)

#challenge
numbers = [5, 2, 5, 2, 2]
myF = "x"
for i in numbers:
    print(i * myF)

#answer
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
    