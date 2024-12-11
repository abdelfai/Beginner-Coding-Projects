#inputs
nPrincipalInvestment = float(input("Enter the starting princpal: "))

nAnnualInterestRate = float(input("Enter the annual interest rate: "))

nNumberOfCompounds = float(input("How many times per year is the interest compounded: "))

nNumberOfPeriods = int(input("For how many years will the account earn interest: "))
#constant
nINTEREST_RATE = nAnnualInterestRate/100
#calculation
nCompound_Interest = nPrincipalInvestment*(1+(nINTEREST_RATE/nNumberOfCompounds))**(nNumberOfCompounds*nNumberOfPeriods)
#outputs
print("At the end of", nNumberOfPeriods, "years you will have $ " + format(nCompound_Interest, ',.2f')) 
      
