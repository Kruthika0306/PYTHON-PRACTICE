d = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
c1 = set(ch)
res = [w for w in d if set(w).issubset(c1)]
print(res)