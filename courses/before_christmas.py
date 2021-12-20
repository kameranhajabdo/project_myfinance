# how to cycle through a dictionary

d = {"a": 1, "b": 2, "c": 4, "d": 8}
for key, value in d.items():
    print(key, value)

#print the keys until a value is bigger than 3
for key, value in d.items():
    if value <= 3:
        print(key)
    else:
        break

def maximum(lista):
    max = lista[0]
    for x in lista:
        if type(x) == str or type(x) == bool:
            continue
        if max < x:
            max = x
    return max

print(maximum([1, "a", 2, 0]))

strings = ["are", "you", "sure", "?"]
sentence = " ".join(strings)
print(sentence)