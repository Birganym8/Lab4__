def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))


gen = squares(a, b)


for square in gen:
    print(square)
