text = input("Enter a sentence: ")

words = text.split()
count = len(words)

print("Total words:", count)

for w in words:
    print(w)

if count > 10:
    print("Long sentence")
else:
    print("Short sentence")
