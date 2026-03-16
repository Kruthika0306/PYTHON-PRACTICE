nums = [1,2,2,3,4,4,5,6]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Original list:", nums)
print("Unique elements:", unique)

print("Total unique:", len(unique))
