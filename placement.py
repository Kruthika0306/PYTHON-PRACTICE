sem=int(input("enter semester"))
branch=input("enter any branch such as CSE or CIVIL").upper() 
match sem:
  case 1 | 3 | 5 | 7 if branch == "CSE":
    print("student is eligible for placement training")
  case 1 | 3 | 5 | 7 if branch == "AIML":
    print("student is eligible for AI training")
  case 2 | 4 | 6  if branch  == "CIVIL":
    print("student is eligible for field visit")
  case 2 | 4 | 6  if branch  == "ECE":
    print("student is eligible for electronics company visit")
  case _:
    print("Eligibility criteria not defined for this case")