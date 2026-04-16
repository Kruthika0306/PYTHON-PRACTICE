file = open("expenses.txt", "a")

for i in range(3):
    item = input("Enter expense name: ")
    cost = input("Enter cost: ")
    file.write(item + "," + cost + "\n")

file.close()

print("\nSaved Expenses:")
file = open("expenses.txt", "r")

total = 0
for line in file:
    name, cost = line.strip().split(",")
    total += float(cost)
    print(name, ":", cost)

print("Total spent:", total)
file.close()
