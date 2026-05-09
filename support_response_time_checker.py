time = int(input("Response time (minutes): "))

if time <= 5:
    print("Excellent response ")
elif time <= 15:
    print("Good response ")
else:
    print("Slow response ")

print("Evaluation done")
