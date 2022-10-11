# Name: - Neeraj Kumar
# ID: - 2047559
import sys

def exact_change(amount_input):
    dollars = amount_input // 100
    quarters = amount_input % 100 // 25
    dimes = amount_input % 100 % 25 // 10
    nickels = amount_input % 100 % 25 % 10 // 5
    pennies = amount_input % 100 % 25 % 10 % 5 // 1
    return dollars,quarters,dimes,nickels,pennies

if __name__ == '__main__':
    amount_input = int(input())

    dollars,quarters,dimes,nickels,pennies = exact_change(amount_input)

    if amount_input <= 0:
        print("no change")
        sys.exit()

    if dollars > 1:
        print(str(dollars) + " dollars")
    elif dollars == 1:
        print(str(dollars) + " dollar")
    else:
        pass
    if quarters > 1:
        print(str(quarters) + " quarters")
    elif quarters == 1:
        print(str(quarters) + " quarter")
    else:
        pass
    if dimes > 1:
        print(str(dimes) + " dimes")
    elif dimes == 1:
        print(str(dimes) + " dime")
    else:
        pass
    if nickels > 1:
        print(str(nickels) + " nickels")
    elif nickels == 1:
        print(str(nickels) + " nickel")
    else:
        pass
    if pennies > 1:
        print(str(pennies) + " pennies")
    elif pennies == 1:
        print(str(pennies) + " penny")