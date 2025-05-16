# Importing math for calculations and data validation
import math

def getFloatInput(sInput):
    
    while True:
        try:
            value = float(input(sInput))
            if value > 0:
                return value
            else:
                print("Value must be greater than zero.")
        except ValueError:
            print("enter a valid number.")

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    
    return math.ceil(fSquareFeet / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
  
    return fLaborHoursPerGallon * iTotalGallons

def getLaborCost(fLaborHours, fLaborChargePerHour):
   
    return fLaborHours * fLaborChargePerHour

def getPaintCost(iTotalGallons, fPaintPrice):
   
    return iTotalGallons * fPaintPrice

def getSalesTax(state):
    # constant for tax rate
    TAX_RATES = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return TAX_RATES.get(state.upper(), 0.0)
#calculating cost estimate
def showCostEstimate(customerLastName, fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, state):
    
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getSalesTax(state)
    fTotalCost = (fLaborCost + fPaintCost) * (1 + fTaxRate)

    #making output
    output = (
        f"Gallons of Paint: {iTotalGallons}\n"
        f"Hours of Labor: {fLaborHours:.2f}\n"
        f"Paint Charges: ${fPaintCost:.2f}\n"
        f"Labor Charges: ${fLaborCost:.2f}\n"
        f"Tax: {fTotalCost/fTaxRate * 100:.2f}\n"
        f"Total Cost: ${fTotalCost:.2f}\n"
    )

    #output
    print(output)
    file_name = f"{customerLastName}_PaintJobOutput.txt"
    print(f"File: {file_name} was created.")

def main():
    
    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")

    state = input("State Job is in: ")
    sCustomerLastName = input("Customer Last Name: ")

    showCostEstimate(sCustomerLastName, fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, state)

if __name__ == "__main__":
    main()
