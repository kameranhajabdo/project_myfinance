if True and False:
    print("yes")
else:
    print("no")


if True or False:
    print("True or False => True")
else:
    print("True or False => False")


if not False:
    print("not Fals = True")
else:
    print("not Fals = Fals")

if 2 == "2":
    print("yes")
else:
    print("no")

if type(2) == type(2.0) or type(2) == type(-56):
    print("True condition")
else:
    print("Fals condition")

if not type(2) == type(2.0) and type(2) == type(0):
    pass

def compute_sum(a, b):
    if type(a) == type(b):
       return a + b
x = compute_sum(1, 1)
print(x)

l = ["a", "b", "c"]
l[0] = "d"
print(l)

d = {"a" : 2 , "b" : 4 , "c" : 7}
s = d["a"] + d["c"]
print(s)

t = (1, 4, 8)
print(t[2])



