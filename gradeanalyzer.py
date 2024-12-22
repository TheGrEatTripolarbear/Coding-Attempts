#NAME
sName = input(f"What is your name?")
#GRADES
fGrade1 = float(input(f"Please input grade one (from 0 - 100):"))
fGrade2 = float(input(f"Please input grade two (from 0 - 100):"))
fGrade3 = float(input(f"Please input grade three (from 0 - 100):"))
fGrade4 = float(input(f"Please input grade four (from 0 - 100):"))
#I think i figured out how ors ands worked more now multiple ors is ok multiple and ors is less so.
if fGrade1 < 0 or fGrade2 < 0 or fGrade3 < 0 or fGrade4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit (f"You can't score the coveted F- that easily.")
if fGrade1 > 100 or fGrade2 > 100 or fGrade3 > 100 or fGrade4 > 100:
    print("Test scores must be less than 100.")
    raise SystemExit (f"You can't score the coveted A++ that easily.")
#Drop the bool except without the true false so not really a bool except everything is a bool if you try hard enough because of the nature of bits
sRaiseTheBaseGradeAverage = input(f"Should this program drop the lowest grade from the average? Capital Y/N")
#I like my philosphy of giving you the user a second chance and a third really as many until you get it right
while sRaiseTheBaseGradeAverage != "Y" and sRaiseTheBaseGradeAverage != "N":
    print (f"We only accept Capital Y for yes or Capital N for no here.")
    sRaiseTheBaseGradeAverage = input(f"Should this program drop the lowest grade from the average? Capital Y/N")
#Math 
if sRaiseTheBaseGradeAverage == "Y":
    if fGrade1 <= fGrade2 and fGrade1 <= fGrade3 and fGrade1 <= fGrade4:
        fFinalGrade = (fGrade2 + fGrade3 + fGrade4) / 3
    elif fGrade2 <= fGrade1 and fGrade2 <= fGrade3 and fGrade2 <= fGrade4:
        fFinalGrade = (fGrade1 + fGrade3 + fGrade4) / 3
    elif fGrade3 <= fGrade1 and fGrade3 <= fGrade2 and fGrade3 <= fGrade4:
        fFinalGrade = (fGrade1 + fGrade2 + fGrade4) / 3
    elif fGrade4 <= fGrade1 and fGrade4 <= fGrade2 and fGrade4 <= fGrade3:
        fFinalGrade = (fGrade1 + fGrade2 + fGrade3) / 3
else: sRaiseTheBaseGradeAverage == "N"
fFinalGrade = (fGrade1 + fGrade2 + fGrade3 + fGrade4) / 4
#Commence lettering this used to be in at least three places in this program if you can beleive that
if fFinalGrade >= 97.0:
        sLetter = "A+"
elif fFinalGrade >= 94.0:
        sLetter = "A"
elif fFinalGrade >= 90.0:
        sLetter = "A-"
elif fFinalGrade >= 87.0:
        sLetter = "B+"
elif fFinalGrade >= 84.0:
        sLetter = "B"
elif fFinalGrade >= 80.0:
        sLetter = "B-"
elif fFinalGrade >= 77.0:
        sLetter = "C+"
elif fFinalGrade >= 74.0:
        sLetter = "C"
elif fFinalGrade >= 70.0:
        sLetter = "C-"
elif fFinalGrade >= 67.0:
        sLetter = "D+"
elif fFinalGrade >= 64.0:
        sLetter = "D"
elif fFinalGrade >= 60.0:
        sLetter = "D-"
else: sLetter = "F"
print(f"{sName}'s final grade is a {fFinalGrade:.1f} it would be the letter grade {sLetter}!")
