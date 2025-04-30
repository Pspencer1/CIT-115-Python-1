def askForwallSpace():
    userWallSpace = float(input("Please enter the square feet of wallspace to be painted: "))
    print()
    return userWallSpace

def askForPriceOfPaint():
    priceOfPaint = float(input("Please enter the price of the paint: "))
    print()
    return priceOfPaint

def askForFeetPerGallon():
  feetPerGallon = float(input("Please enter the feet per gallon: "))
  print()
  return feetPerGallon
  
if __name__ == "__main__":
  result = askForFeetPerGallon()
  

def askForHoursPerGallon():
    hoursPerGallon = float(input("Please enter the hours per gallon: "))  
    print()
    return hoursPerGallon  

if __name__ == "__main__":
  result = askForHoursPerGallon()
    

def askForLaborChargePerHour()  :
    laborChargePerHour = float(input("Please enter the labor charge per hour: "))
    print()
    return laborChargePerHour

if __name__ == "__main__":
  result = askForLaborChargePerHour()

def askWhatStateJobIsIn()  :
    state = input("Please enter the state: ")
    print()  
    return state
if __name__ == "__main__":
  result = askWhatStateJobIsIn()
  
def whatIsYourName()  :
    name = input("Please enter your name: ")
    print()
    return name
if __name__ == "__main__":
  result = whatIsYourName()

def calculatePaintRequired(userWallSpace):
    paintRequired = userWallSpace / 112 * 1
    return paintRequired

def calculateGallonsOfPaintRequired(userWallSpace): 
    gallonsOfPaintRequired = userWallSpace / 112
    return gallonsOfPaintRequired

def calculateHoursOfLaborRequired(userWallSpace):  
    hoursRequired = (userWallSpace / 112) * 8
    return hoursRequired

def calculateCostOfPaint(priceOfPaint, gallonsOfPaintRequired):  
    costOfPaint = gallonsOfPaintRequired * priceOfPaint
    return costOfPaint

def calculateLaborCharges(hoursOfLaborRequired): 
    CHARGE_PER_HOUR = 35.00
    laborCharges = hoursOfLaborRequired * CHARGE_PER_HOUR  
    return laborCharges

def calculateTotalCostOfPaintJob(laborCharges, costOfPaint):
    totalCost = laborCharges + costOfPaint
    return totalCost

def printBill(paintRequired, hoursRequired, costOfPaint, laborCharges, totalCost):  
    print("Paint required:", format(paintRequired, ".2f"))
    print("Hours of labor required:", format(hoursRequired, ".2f"))
    print("Cost of the paint: $" + format(costOfPaint, ",.2f"))
    print("Labor charges: $" + format(laborCharges, ",.2f"))
    print("Total Cost: $" + format(totalCost, ",.2f"))
    print()
    print("Thank you for using the paint calculator!")  
    print("Have a great day!")
    print()
    print("Goodbye!")
    print()  
    print("End of program")  



def main():  
    userWallSpace = askForwallSpace()
    priceOfPaint = askForPriceOfPaint()
    paintRequired = calculatePaintRequired(userWallSpace)
    hoursRequired = calculateHoursOfLaborRequired(userWallSpace)
    costOfPaint = calculateCostOfPaint(priceOfPaint, paintRequired)
    laborCharges = calculateLaborCharges(hoursRequired)
    totalCost = calculateTotalCostOfPaintJob(laborCharges, costOfPaint)  
    printBill(paintRequired, hoursRequired, costOfPaint, laborCharges, totalCost)  

main()  
