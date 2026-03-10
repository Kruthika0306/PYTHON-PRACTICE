n = int(input("Enter a decimal number: "))
count = 0

while n > 0:
    n = n // 2
    count += 1

print("Number of binary digits required:", count)