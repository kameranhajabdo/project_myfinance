f = lambda x: x + 1

print(f(5))

def xplus1(l: list) -> list:
    return [f(x) for x in l]

p = xplus1([5,6,7,8])
print(p)
