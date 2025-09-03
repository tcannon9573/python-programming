num = input("Enter a number: ")
squares = []
for i in range(1, int(num) + 1):
    squares.append(i**2)
    print(i ** 2, end = "")
    if i == int(num):
        print("\n")
    else:
        print(",", end ="")
    print(squares)