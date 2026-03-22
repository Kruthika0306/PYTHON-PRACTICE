import os

filename = input("Enter file name to search: ")
files = os.listdir()

found = False

for file in files:
    if filename in file:
        print("Found:", file)
        found = True

if not found:
    print("File not found ")
