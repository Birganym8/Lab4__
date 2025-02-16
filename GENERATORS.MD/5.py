def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter the number: "))


gen = countdown_generator(n)


for number in gen:
    print(number)
