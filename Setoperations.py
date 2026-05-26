# Taking user input

set1 = set(map(int, input("Enter elements of Set 1: ").split()))
set2 = set(map(int, input("Enter elements of Set 2: ").split()))

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union
print("\nUnion:")
print(set1.union(set2))

# Intersection
print("\nIntersection:")
print(set1.intersection(set2))

# Difference
print("\nDifference (Set1 - Set2):")
print(set1.difference(set2))

# Difference
print("\nDifference (Set2 - Set1):")
print(set2.difference(set1))

# Symmetric Difference
print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))

# Subset check
print("\nIs Set1 subset of Set2?")
print(set1.issubset(set2))

# Superset check
print("\nIs Set1 superset of Set2?")
print(set1.issuperset(set2))
