def square_generator(N):
    for i in range(N + 1):
        yield i * i


for square in square_generator(10):
    print(square)
