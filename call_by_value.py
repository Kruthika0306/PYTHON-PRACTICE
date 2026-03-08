def modify(x):
    x = x + 10
    print("Inside function:", x)

a = 5  # immutable object, act like call by value
modify(a)
print("Outside function:", a)