def rgb(r, g, b):
  return f"\033[38;2;{r};{g};{b}m"

def getBalace(balance):
    print(f"{rgb(0,255,0)}Your current balance is Nrs {balance:.2f} {reset}")

def withdraw(balance):
    amt = float(input("Enter amount you wish to withdraw: "))

    if amt < 0:
        print("***************************")
        print(f"{rgb(255,0,0)}You can not withdraw less than 0.{reset}")
        return 0
    elif amt > balance:
        print("***************************")
        print(f"{rgb(255,0,0)}Insufficient balance for withdrawal.{reset}")
        return 0
    else:
        print("***************************")
        print(f"{rgb(0, 200, 0)}Success!{reset}")
        return amt


def deposit():
    amt = float(input("Enter amount you wish to deposit: "))

    if amt <= 0:
        print("***************************")
        print(f"{rgb(255,0,0)}You can not deposit less than 0.{reset}")
        return 0
    else:
        print("***************************")
        print(f"{rgb(0, 200, 0)}Success!{reset}")
        return amt

def main():
    balance = 0
    is_processing = True

    while is_processing:
        print("***************************")
        print("Welcome to Simple Banking Program.")
        print("***************************")
        print("1. Check Balance.")
        print("2. Deposit.")
        print("3. Withdrawal.")
        print("4. EXIT app.")
        print("***************************")
        choice = input("Choose between (1 to 4): ")
        print("***************************")

        if choice == '1':
            getBalace(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_processing = False
        else:
            print(f"{rgb(255,0,0)}Err!! Invalid choice option!!{reset}")

    print("***************************")
    print(f"{rgb(0, 255,255)}Thank you. Have a great day.{reset}")
    print("***************************")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reset = "\033[0m"
    main()