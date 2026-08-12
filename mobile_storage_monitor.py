total = 128
used = 97

free = total - used

print("Used Storage:", used, "GB")
print("Free Storage:", free, "GB")

if free < 15:
    print("Storage Running Low")
