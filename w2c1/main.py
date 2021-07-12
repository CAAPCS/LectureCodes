

# get the total bill from user
def getTotalBill():
    print("Make sure to type a number, otherwise things will break!")
    total_bill = input("What was your total bill? ") # this is a string
    total_bill = float(total_bill) #this is now a float
    return total_bill

def displayBillResults(total_bill, computed_tip, tip):
    print('>>>>>>>>>>>>>>')
    print("TOTAL COST:", total_bill + computed_tip)
    print("\tFOOD COST:", total_bill)
    print("\tTIP:", computed_tip)
    print('>>>>>>>>>>>>>>')
    print("btw we used this as tip", tip)

# compute the tip amount
def computeTipFromBill(amount, tip):
    return amount * tip

def getTip():
    tip = input("hey what tip do you want to give? ")
    # tip -> string
    if '%' == tip[-1]:
        tip_without_percent = tip[:-1]
        tip = float(tip_without_percent)  / 100.0
    else:
        tip = float(tip)
    return tip



if __name__ == '__main__':
    amount_of_bill = getTotalBill()
    tip = getTip()
    computed_tip = computeTipFromBill(amount_of_bill, tip)
    displayBillResults(amount_of_bill, computed_tip, tip)
