# prompt user for input
# temperature (number)
# temperature format (F/C)

fTemperature= float(input(" Enter a temperature: "))
sTempType= input("Is the temp F for Fahrenheit or C for Celsius?")

#process calculations
fFahrenheit=((9.0/5.0)*fTemperature +32)
fCelsius= (5.0/ 9) * (fTemperature - 32)

if sTempType== 'F' or sTempType == 'f':
    if fTemperature > 212:
        print("temperature can not be > 212")
    elif fTemperature<= 212:
            print(f"The Celsius equivalent is: {fCelsius}")
    elif sTempType== 'C' or sTempType == 'C':
        if fTemperature > 100:
            print("Temperature can not be > 100")
    elif fTemperature <= 100:
        print(f"The Celsius equivalent is: {fFahrenheit}")
    else:
            print("enter F or C")
            