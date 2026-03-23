balance = 1000

while True:
    print("\n1.Deposit  2.Withdraw  3.Check  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        amt = int(input("Amount: "))
        balance += amt
    elif choice == "2":
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
    elif choice == "3":
        print("Balance:", balance)
    else:
        break
