def main():
    amount = 50
    remaining = 50
    paid_amount = 0
    coke_cost = 50

    while paid_amount < coke_cost:
        p = int(input("How much money are you putting in"))
        if p != 25 and p != 5 and p != 10:
            print("Incorrect try again!")
        else:
            paid_amount += p
            remaining = coke_cost - paid_amount
            if remaining > 0:
                print("amount due:", remaining)
    else:
        print("here is your change", "$", abs(remaining))


main()
