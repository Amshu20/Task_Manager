b = 0  # global balance


def manager():
    global b
    print("You can \n1)Check Balance\n2)Deposit\n3)Withdraw\n4)Exit")
    c = int(input("Enter your choice: "))

    if c == 1:
        print("Your balance is:", b, "\n")
    elif c == 2:
        d = int(input("Enter amount to deposit: "))
        b += d
    elif c == 3:
        w = int(input("Enter amount to withdraw: "))
        if b < w:
            print("Insufficient funds")
        else:
            b -= w
    elif c == 4:
        print("Exiting...")
        return
    else:
        print("Invalid choice")

    manager()  # call again for next operation


def main():
    print("Welcome to account manager")
    manager()


main()