import time

seconds = int(input("Enter seconds: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("Time's up!")
print("Countdown finished")
