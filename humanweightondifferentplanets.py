# Weight constants
fMERCURY  = .38
fVENUS    = .91
fMOON     = .165
fMars     = .38
fJUPITER  = 2.34
fSATURN   = .93
fURANUS   = .92
fNEPTUNE  =1.12
fPLUTO    = .066

# Input for first person
sName = input("what is your name? ")
fErthWghT1 = float(input(f"{sName} how much do you weigh: "))

# Calculations
fMercuryWeight = fErthWghT1 * fMERCURY
fVENUSWeight   = fErthWghT1 * fVENUS
fMoonWeight    = fErthWghT1 * fMOON
fMarsWeight    = fErthWghT1 * fMars
fJupiterWeight = fErthWghT1 * fJUPITER
fSaturnWeight  = fErthWghT1 * fSATURN
fUranusWeight  = fErthWghT1 * fURANUS
fNeptuneWeight = fErthWghT1 * fNEPTUNE
fPlutoWeight   = fErthWghT1 * fPLUTO

#output
print(f"{sName} human weight on different planets of our solar system")
print(f"{'Mercury weight:':25s} {fMercuryWeight:10,.2f}")
print(f"{'Venus weight:':25s} {fVENUSWeight:10,.2f}")
print(f"{'Moon weight:':25s} {fMoonWeight:10,.2f}")
print(f"{'Mars weight:':25s} {fMarsWeight:10,.2f}")
print(f"{'Jupiter weight:':25s} {fJupiterWeight:10,.2f}")
print(f"{'Saturn weight:':25s} {fSaturnWeight:10,.2f}")
print(f"{'Uranus weight:':25s} {fUranusWeight:10,.2f}")
print(f"{'Neptune weight:':25s} {fNeptuneWeight:10,.2f}")
print(f"{'Pluto weight:':25s} {fPlutoWeight:10,.2f}")
