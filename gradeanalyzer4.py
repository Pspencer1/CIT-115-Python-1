# The student's name
strName = input("Enter the student's name: ")

# four test scores
intTest1 = int(input("Enter test score 1: "))
intTest2 = int(input("Enter test score 2: "))
intTest3 = int(input("Enter test score 3: "))
intTest4 = int(input("Enter test score 4: "))



# drop the lowest score
strDropLowest = input("Drop the lowest grade? (Y/N): ")

# lowest drop
if strDropLowest.upper() != "Y" and strDropLowest.upper() != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Calculate the average
if strDropLowest.upper() == "Y":
    # Find the lowest score (without using min() or lists)
    if intTest1 <= intTest2 and intTest1 <= intTest3 and intTest1 <= intTest4:
        lowestScore = intTest1
    elif intTest2 <= intTest1 and intTest2 <= intTest3 and intTest2 <= intTest4:
        lowestScore = intTest2
    elif intTest3 <= intTest1 and intTest3 <= intTest2 and intTest3 <= intTest4:
        lowestScore = intTest3
    else:
        lowestScore = intTest4

    # Calculate 3 scores
    if lowestScore == intTest1:
        fltAverage = float((intTest2 + intTest3 + intTest4) / 3)
    elif lowestScore == intTest2:
        fltAverage = float((intTest1 + intTest3 + intTest4) / 3)
    elif lowestScore == intTest3:
        fltAverage = float((intTest1 + intTest2 + intTest4) / 3)
    else:
        fltAverage = float((intTest1 + intTest2 + intTest3) / 3)

else:
    # Calculate 4 scores
    fltAverage = float((intTest1 + intTest2 + intTest3 + intTest4) / 4)

# letter grade
if fltAverage >= 97.0:
    strLetterGrade = "A+"
elif fltAverage >= 94.0:
    strLetterGrade = "A"
elif fltAverage >= 90.0:
    strLetterGrade = "A-"
elif fltAverage >= 87.0:
    strLetterGrade = "B+"
elif fltAverage >= 84.0:
    strLetterGrade = "B"
elif fltAverage >= 80.0:
    strLetterGrade = "B-"
elif fltAverage >= 77.0:
    strLetterGrade = "C+"
elif fltAverage >= 74.0:
    strLetterGrade = "C"
elif fltAverage >= 70.0:
    strLetterGrade = "C-"
elif fltAverage >= 67.0:
    strLetterGrade = "D+"
elif fltAverage >= 64.0:
    strLetterGrade = "D"
elif fltAverage >= 60.0:
    strLetterGrade = "D-"
else:
    strLetterGrade = "F"

# Output 
print(f"{strName}'s average is: {fltAverage:.1f}")
print(f"Letter Grade: {strLetterGrade}")