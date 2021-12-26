
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

def removes_odd_number(dict1):
    for x in dict1:
        if x%2!=0:
            dict1.remove(x)
print(removes_odd_number(dict1))
