cs_department = {"Asha", "Ravi", "John", "Meena", "Kiran"}
coding_club = {"Ravi", "John"}
print("All club members are from CS:", coding_club.issubset(cs_department))
print("CS dept contains all club members:", cs_department.issuperset(coding_club))