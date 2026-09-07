#pset2-coke
def main():
    print ("Amount due: 50")
    total_paid = 0
    while True:
        coins = int(input("Insert coin: "))
        if coins == 25 or coins == 10 or coins == 5:
            total_paid += coins
            amount_due = 50 - total_paid
            if amount_due > 0:
                print(f"Amount due: {amount_due}")
            else:
                change = -amount_due
                print(f"Change owed: {change}")
                break

main()