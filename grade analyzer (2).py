# Grade Analyzer

#inputs

sName = input("Name of person that we are calculating the grades for: ")
iTestOne = int(input("Test 1: "))
iTestTwo = int(input("Test 2: "))
iTestThree = int(input("Test 3: "))
iTestFour = int(input("Test 4: "))

sDrop = input("Do you wish to Drop the Lowest Grade Y or N? ")

if iTestOne < 0 or iTestTwo < 0 or iTestThree < 0 or iTestFour < 0:
    print("Test scores must be greater than 0. ")
    raise SystemExit

#calculations
 # could have just let us use that min function man 😂   
if sDrop == ("Y"):
    if iTestOne < (iTestTwo and iTestThree and iTestFour):
        fAverage = (iTestTwo + iTestThree + iTestFour) / 3
    elif iTestTwo < (iTestOne and iTestThree and iTestFour):
        fAverage = (iTestOne + iTestThree + iTestFour) / 3
    elif iTestThree < (iTestOne and iTestTwo and iTestFour):
        fAverage = (iTestOne + iTestThree + iTestFour) / 3
    elif iTestFour < (iTestOne and iTestTwo and iTestThree):
        fAverage = (iTestOne + iTestTwo + iTestThree) / 3

if sDrop == ("N"):
    fAverage = (iTestOne + iTestTwo + iTestThree + iTestFour) / 4

elif sDrop != ("Y" or "N"):
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

#outputs
# i didnt give constants to the grades i dont think its necessary, extra lines of code
if fAverage <= 59.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is: F")
if fAverage > 59.9 and fAverage <= 63.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is: D-")
if fAverage > 63.9 and fAverage <= 66.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is D")
if fAverage > 66.9 and fAverage <= 69.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is D+")
if fAverage > 69.9 and fAverage <= 73.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is C-")
if fAverage > 73.9 and fAverage <= 76.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is C")
if fAverage > 76.9 and fAverage <= 79.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is C+")
if fAverage  > 79.9 and fAverage <= 83.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is B-")
if fAverage > 83.9 and fAverage <= 86.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is B")
if fAverage > 86.9 and fAverage <= 89.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is B+")
if fAverage > 89.9 and fAverage <= 93.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is A-")
if fAverage > 93.9 and fAverage <= 96.9:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade for the test is A")
if fAverage >= 97:
    print(f"{sName} test average is {fAverage:.1f}")
    print("Letter Grade is A+")


    
    
    
    

    
