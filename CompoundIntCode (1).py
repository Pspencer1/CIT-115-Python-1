# FV = PV (1+ R/M)**mt
#input (prompt user for variables)
fPrincpal = float(input("How much is the starting princpal?: ")) # PV
fRate = float(input("How much is the annual intrest rate?: ")) # R
fTimesPerYear = float(input("How many times per year is the intrest compounded?: ")) # T
iYearsInt = int(input("How many years will the account earn intrest?: ")) # M

#process (calculations)
fFutureValue = fPrincpal * (1 + (fRate / 100) / iYearsInt) ** (fTimesPerYear * iYearsInt)

#output
print(f"At the end of {iYearsInt} years you will have $ {fFutureValue:,.2f}")