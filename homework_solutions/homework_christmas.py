
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

for key, value in dict1.items():
    if value % 2 != 0:
        del dict1[key]
        break

print(dict1)

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


#ex7
prices = {"iphone": 1000, "samsung": 800, "pixel": 600, "allview": 100, "nokia": 200, "oppo": 600}

def get_phones(phones: dict, min: int, max: int):
    lista = []
    for key, value in phones.items():
        if min <= value <= max:
            lista.append(key)
    return lista

#ex8

accounts = [
    {"user": "Bob", "account": 0, "debt": 500},
    {"user": "Alice", "account": 2000, "debt": 0},
    {"user": "Leo", "account": 600, "debt": 2000},
    {"user": "Ralph", "account": 5000, "debt": 1000},
    {"user": "Matilda", "account": 100, "debt": 0}
]
max_account = None

for user in accounts:
    if not max_account:
        max_account = user
    if max_account and max_account["account"] < user["account"]:
        max_account = user

print(max_account["user"])
max_dif = None
for user in accounts:
    if not max_dif:
        max_dif = user
    elif max_dif ["debt"] - max_dif["account"] < user["account"]:
        max_dif = user
print(max_dif["user"])

#ex9

user = input("what is your name?")
email = input("what is your email?")
tel = input("what is your phone number?")

d = {"user": user, "email": email, "tel":tel}

print(d)

#ex10

def rock_paper_scissors():
    import random
    computer = random.choice(["rock", "paper","scissors"])
    user = input("pick rock , paper or scissors:")
    if computer == user:
        print("egalitate")
    elif (user == "rock" and computer == "scissors") \
            or (user == "scissors" and computer == "paper") \
            or (user == "paper" and computer == "rock"):
        print("you won!" + computer)
    else:
        print("the computer won" + computer)

rock_paper_scissors()

