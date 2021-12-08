def print_all_elements(lista):
   for x in lista:
     if type(x) == int:
        print(x)

l = [1, 2, "a", "b"]
print_all_elements(l)

tu = (1, 2, 3)
print_all_elements(tu)