# Constants
nCELSIUS_CONSTANT = (5.0/9)
nFAHRENHEIT_CONSTANT = (9.0/5.0)
# input and output

sTemp = float(input("Enter a temperature: "))
sType = input("Is the temp F for Fahrenheit or C for Celsius? ")
if sType == "F" and sTemp <= 212:
    nFahrenheit = nCELSIUS_CONSTANT * (sTemp - 32)
    print(f"The Celsius equivalent is: {nFahrenheit:.1f}")
elif sType == "F" and sTemp > 212:
    print("Temp can not be > 212")
elif sType == "C" and sTemp <= 100:
    nCelsius = (nFAHRENHEIT_CONSTANT * sTemp) + 32
    print(f"The Fahrenheit equivalent is: {nCelsius:.1f}")
elif sType == "C" and sTemp > 100:
    print("Temp can not be > 100")
else:
    print("Enter a F or C")
    raise SystemExit
          


# this one stumped me a little, was there any easier way to code this? any tips would be appreciated.
