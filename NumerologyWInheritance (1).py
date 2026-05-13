class Numerology:

    def __init__(self, name, bday):

        #name
        if name.strip() == "":
            print("Name can't be empty")
            self._name = "none"
        else:
            self._name = name.upper()

        #date
        bday = bday.replace("/", "-")

        parts = bday.split("-")

        if len(parts) != 3:
            print("wrong date")
            self._bday = "01-01-2000"
        else:
            digits = ""

            for ch in bday:
                if ch.isdigit():
                    digits = digits + ch

            if len(digits) != 8:
                print("Date needs 8 digits")
                self._bday = "01-01-2000"
            else:
                self._bday = bday

    def reduce(self, num):
        while num > 9:
            total = 0
            for i in str(num):
                total = total + int(i)
            num = total
        return num

    def value(self, ch):
        if ch == "A" or ch == "J" or ch == "S":
            return 1
        elif ch == "B" or ch == "K" or ch == "T":
            return 2
        elif ch == "C" or ch == "L" or ch == "U":
            return 3
        elif ch == "D" or ch == "M" or ch == "V":
            return 4
        elif ch == "E" or ch == "N" or ch == "W":
            return 5
        elif ch == "F" or ch == "O" or ch == "X":
            return 6
        elif ch == "G" or ch == "P" or ch == "Y":
            return 7
        elif ch == "H" or ch == "Q" or ch == "Z":
            return 8
        elif ch == "I" or ch == "R":
            return 9
        else:
            return 0

    @property
    def Name(self):
        return self._name

    @property
    def Birthdate(self):
        return self._bday

    @property
    def LifePath(self):
        total = 0
        for ch in self._bday:
            if ch.isdigit():
                total = total + int(ch)
        return self.reduce(total)

    @property
    def BirthDay(self):
        parts = self._bday.split("-")
        day = int(parts[1])
        return self.reduce(day)

    @property
    def Attitude(self):
        parts = self._bday.split("-")
        month = int(parts[0])
        day = int(parts[1])
        return self.reduce(month + day)

    @property
    def Soul(self):
        total = 0
        for ch in self._name:
            if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
                total = total + self.value(ch)
        return self.reduce(total)

    @property
    def Personality(self):
        total = 0
        for ch in self._name:
            if ch.isalpha():
                if not (ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"):
                    total = total + self.value(ch)
        return self.reduce(total)

    @property
    def PowerName(self):
        return self.reduce(self.Soul + self.Personality)

    def __str__(self):
        text = ""
        text += "Client Name: " + self.Name + "\n"
        text += "Client DOB: " + self.Birthdate + "\n"
        text += "Life Path: " + str(self.LifePath) + "\n"
        text += "Attitude: " + str(self.Attitude) + "\n"
        text += "Birthday: " + str(self.BirthDay) + "\n"
        text += "Personality: " + str(self.Personality) + "\n"
        text += "Power Name: " + str(self.PowerName) + "\n"
        text += "Soul: " + str(self.Soul)
        return text


class NumerologyLifePathDetails(Numerology):

    @property
    def LifePathDescription(self):

        num = self.LifePath

        if num == 1:
            return "Independent: Wants to work or think for themselves"
        elif num == 2:
            return "Mediator: Avoids conflict and wants harmony"
        elif num == 3:
            return "Performer: Likes art and attention"
        elif num == 4:
            return "Teacher or Truth Seeker"
        elif num == 5:
            return "Adventurer"
        elif num == 6:
            return "Inner Child"
        elif num == 7:
            return "Naturalist"
        elif num == 8:
            return "Executive"
        elif num == 9:
            return "Humanitarian"
        else:
            return "none"


name = input("name: ")
bday = input("birthday (mm-dd-yyyy): ")

person = NumerologyLifePathDetails(name, bday)

print()
print(person)
print("Life Path Description:", person.LifePathDescription)