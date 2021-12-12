def say_hello_to_all(list_of_names):
    for x in list_of_names:
        print("hello " + x)

names = ["Bob", "Jane", "Bill", "George", "Ryan"]
say_hello_to_all(names)

def print_only_odd_numbers(list_of_numbers):
    for x in list_of_numbers: # print only the odd numbers from the list (numerele impare)
        if x % 2 !=0:
           print(x)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)

