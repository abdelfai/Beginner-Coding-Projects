#inputs

fDeposit = 0

# Loop to get a valid positive deposit value
while fDeposit <= 0:
    try:
        fDeposit = float(input("What is the original deposit (positive value): "))
        if fDeposit <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value.")

fInterestRate = 0

# Loop to get a valid positive interest rate
while fInterestRate <= 0:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
        if fInterestRate <= 0:
            print("Input must be a positive numeric value.")
    except ValueError:
        print("Input must be a positive numeric value.")

iMonths = 0

while iMonths <= 0:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input mustbe a positive numeric value and whole number.")
    except ValueError:
        print("Input must be a positive numeric value and whole number.")

fGoal = -1

while fGoal < 0:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("Input must be 0 or greater.")
    except ValueError:
        print("Input must be 0 or greater.")
#calculations
        
fINTEREST_DECIMAL = fInterestRate / 100

fMonthInterestRate = fINTEREST_DECIMAL / 12
fAccountBalance = fDeposit
#outputs and loops

for iMonths in range (1, iMonths + 1):
    fInterestForMonth = fAccountBalance * fMonthInterestRate
    fAccountBalance += fInterestForMonth
    print(f"Month:  {iMonths}  Account Balance is: $ {fAccountBalance:,.2f}")

iMonthsItTakes = 0
fAccountBalance = fDeposit
while fAccountBalance < fGoal:
    fInterestForMonth = fAccountBalance * fMonthInterestRate
    fAccountBalance += fInterestForMonth
    iMonthsItTakes  += 1
print(f"It will take: {iMonthsItTakes} months to reach the goal of $ {fGoal:,.2f}")


#hopefully there isnt a assigment harder than this one 😂
    

