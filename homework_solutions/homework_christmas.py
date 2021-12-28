
# ex1 - define a function which returns the keys of a dictionary as a list
# ex2 - define a function which returns the biggest number from a dictionary
# ex3 - define a function which removes all odd numbers from a dictionary

#ex1
def keys_as_a_list(dict1):
    return dict1.keys()

dict1 = {"a": 1, "b": 3, "c": 6, "d": 10, "e": 90, "f": 15}

print(keys_as_a_list(dict1))

#ex2

dict1 = {"a": 1, "b": 3, "c": 6, "d": 10, "e": 90, "f": 15}
biggest_number = max(dict1, key=dict1.get)
print(biggest_number)

#ex3
dict1 = {"a": 1, "b": 3, "c": 6, "d": 10, "e": 90, "f": 15}

#ex4

tuple1 = ("a", "b", "c", "d")
tuple2 = (1, 2, 3, 4)

dict = {}
for key, value in enumerate(tuple1):
    dict[value] = tuple2[key]
print(dict)


#ex5

def sum_of_value(dict11):
    l = []
    for x in dict11:
        l.append(dict11[x])
    final = sum(l)

    return final


dict1 = {"a": 1, "b": 3, "c": 6, "d": 10, "e": 90, "f": 15}
print(sum_of_value(dict1))


