# Ask for class or work length in minutes.
# Determine hours and minutes length

# Declare a constant of 60 minutes in a hour: 
nMINUTES_IN_HOUR = 60

#1. Input:
sInput = input("How many minutes is your class or work shift in whole numbers: ")

#2. Convert:

# 3. Compute

# 3.1 get hours using integer division:


# 3.2 get minutes using modulus division to get remainder
#     as a whole number:

# 4. Output:

print(iInputtedMinutes, "minutes is:", iHours, "hour(s) and", iMinutes, "minutes")

# or you can use string concatenation: 
print(str(iInputtedMinutes) + " minutes is: " + str(iHours) + " hour(s) and " + str(iMinutes) +  " minutes")
      
