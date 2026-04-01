import os

folder = "."
total_size = 0

for file in os.listdir(folder):
    if os.path.isfile(file):
        size = os.path.getsize(file)
        total_size += size

print("Total folder size:", total_size, "bytes")

print("Calculation complete")
