def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Input a number that is greater than 0.")
        except ValueError:
            print("Please enter a valid number that is greater than 0.")

def getMedian(values):
    number = len(values)
    if number % 2 == 1:
        #finding median for an odd number
        MIDDLE_INDEX = number // 2
        return values[MIDDLE_INDEX]
    else:
        #finding median for an even number
        MIDDLE_INDEX1 = number // 2 - 1
        MIDDLE_INDEX2 = number // 2
        return (values[MIDDLE_INDEX1] + values[MIDDLE_INDEX2]) / 2
#assigning the property counter for loop below
def main():
    sales = []
    PROP_COUNTER= 1 

    while True:
        sales_price = getFloatInput("Enter property sales value: ")
        sales.append(sales_price)
#asking for another value
        while True:
            another = input("Enter another value Y or N: ").strip().lower()
            if another == "y":
                break
            elif another == "n":
                break
            else:
                print("Enter Y or N")
        
        if another == "n":
            break
    
    sales.sort()

    # looping the property counter
    for sale in sales:
        print(f"Property {PROP_COUNTER}: ${sale:,.2f}")
        PROP_COUNTER += 1
#calculations
    fMinSales = min(sales)
    fMaxSales = max(sales)
    fTotalSales = sum(sales)
    fAverageSales= fTotalSales / len(sales)
    fMedianSales = getMedian(sales)
    fComission = fTotalSales * 0.03
#outputs
    print(f"\nMinimum: ${fMinSales:,.2f}")
    print(f"Maximum: ${fMaxSales:,.2f}")
    print(f"Total: ${fTotalSales:,.2f}")
    print(f"Average: ${fAverageSales:,.2f}")
    print(f"Median: ${fMedianSales:,.2f}")
    print(f"Commission: ${fComission:,.2f}")

if __name__ == "__main__":
    main()

