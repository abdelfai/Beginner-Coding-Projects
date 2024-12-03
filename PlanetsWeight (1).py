# all the constants
nMERCURY_GRAVITY = 0.38
nVENUS_GRAVITY = 0.91
nMOON_GRAVITY = 0.165
nMARS_GRAVITY = 0.38
nJUPITER_GRAVITY = 2.34
nSATURN_GRAVITY = 0.93
nURANUS_GRAVITY = 0.92
nNEPTUNE_GRAVITY = 1.12
nPLUTO_GRAVITY = 0.066
#input
sName = input("What is your name: ")
nWeight = float(input("What is your weight: "))
#calculations
nMercuryWeight = nWeight * nMERCURY_GRAVITY
nVenusWeight = nWeight * nVENUS_GRAVITY
nMoonWeight = nWeight * nMOON_GRAVITY
nMarsWeight = nWeight * nMARS_GRAVITY
nJupiterWeight = nWeight * nJUPITER_GRAVITY
nSaturnWeight = nWeight * nSATURN_GRAVITY
nUranusWeight = nWeight * nURANUS_GRAVITY
nNeptuneWeight = nWeight * nNEPTUNE_GRAVITY
nPlutoWeight = nWeight * nPLUTO_GRAVITY
#ouput
print((sName), "here are your weights on our Solar System's planets: ")
print ("Weight on Mercury: " + format(nMercuryWeight, '10.2f'))
print ("Weight on Venus:   " + format(nVenusWeight, '10.2f'))
print ("Weight on Moon:    " + format(nMoonWeight, '10.2f'))
print ("Weight on Mars:    " + format(nMarsWeight, '10.2f'))
print ("Weight on Jupiter: " + format(nJupiterWeight, '10.2f'))
print ("Weight on Saturn:  " + format(nSaturnWeight, '10.2f'))
print ("Weight on Uranus:  " + format(nUranusWeight, '10.2f'))
print ("Weight on Neptune: " + format(nNeptuneWeight, '10.2f'))
print ("Weight on Pluto:   " + format(nPlutoWeight, '10.2f'))

# :) 
