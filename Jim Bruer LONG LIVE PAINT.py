# MardiGras gets floats
def MardiGras(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a POSITIVE NUMBER.")
        except ValueError:
            print("Wrong, NUMBERS only.")

# Circles are round
def Circle(value):
    return int(value) + (value % 1 > 0)

# For states that don't exist like New Hampshire, Old Hampshire Fans stay winning
def realStates(sTaxes):
    if sTaxes == "CT" or sTaxes == "VT":
        return 0.06
    elif sTaxes == "MA":
        return 0.0625
    elif sTaxes == "ME":
        return 0.085
    elif sTaxes == "RI":
        return 0.07
    else:
        return 0.0

def getGallonesOfPaint(fSquareFeet, fFeetPerGallone):
    return Circle(fSquareFeet / fFeetPerGallone)

# Unnecessary expenses if you have a small wall
def getLaborHours(fPaintTime, totalGallones):
    return fPaintTime * totalGallones

# defs
def getLaborCost(fLaborHours, fUnneccesaryExpense):
    return fLaborHours * fUnneccesaryExpense

# Defs!
def getPaintCost(totalGallones, fPaintPrice):
    return totalGallones * fPaintPrice

# DEFS!!!
def showCostEstimate(gallones, laborHours, laborCost, paintCost, taxRate, lastName):
    taxAmount = paintCost * taxRate
    totalCost = laborCost + paintCost + taxAmount
    output = (
        f"Gallons of Paint: {gallones}\n"
        f"Your labor hours are: {laborHours:.2f}\n"
        f"Your labor cost is: ${laborCost:.2f}\n"
        f"Your paint cost is: ${paintCost:.2f}\n"
        f"Your tax amount is: ${taxAmount:.2f}\n"
        f"Your tax rate is: {taxRate:.2%}\n"
        f"Finally, your total price is: ${totalCost:.2f}\n"
    )
    print(output)
#couldnt get tax ammount the same as sample output was I supposed to tax labor rates aswell?
    filename = f"{lastName}_PaintJobOutput.txt"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"And your file has been created and saved as {filename}.")

# Main does a little bit of everything
def Main():
    fSquareFeet = MardiGras("How Big is your wall in square feet?: ")
    fPaintPrice = MardiGras("How much does paint cost?: ")
    fFeetPerGallone = MardiGras("How many feet will a gallon of your paint cover?: ")
    fPaintTime = MardiGras("How many labor hours per gallon of paint?: ")
    fUnneccesaryExpense = MardiGras("How much do painters in your area charge per hour?: ")

    sTaxes = input("Which state will this take place in? (Please use capital abbreviations like: CT, MA, ME, NH, RI, VT): ").upper()

    lastName = input("What is your last name?: ")

    # Your gaaallllonnnes
    iGallonesNeeded = getGallonesOfPaint(fSquareFeet, fFeetPerGallone)

    # The prices you need
    fLaborHours = getLaborHours(fPaintTime, iGallonesNeeded)
    fLaborCost = getLaborCost(fLaborHours, fUnneccesaryExpense)
    fPaintCost = getPaintCost(iGallonesNeeded, fPaintPrice)
    fSalesTaxRate = realStates(sTaxes)

    showCostEstimate(iGallonesNeeded, fLaborHours, fLaborCost, fPaintCost, fSalesTaxRate, lastName)
#it does the thing
Main()
