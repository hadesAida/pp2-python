def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")
print()


def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_generator(n))))


def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
for num in div_by_3_and_4(n):
    print(num, end=" ")
print()

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter start number: "))
b = int(input("Enter end number: "))

for square in squares(a, b):
    print(square)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")
print()
