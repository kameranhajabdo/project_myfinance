
def is_divisible(number, divisor):
    return number % divisor == 0

print(is_divisible(7, 3))
print(is_divisible(100, 10))


def ex2(nr):
    if nr % 2 == 0:
        return nr / 2
    else:
        return nr * 3
