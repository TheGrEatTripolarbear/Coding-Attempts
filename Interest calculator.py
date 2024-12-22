#Asking all the starter questions
#fPrincipal = float(input(f"Enter the starting principal:"))
#fInterestRate = float(input(f"Enter the annual interest rate:"))
#iComp = int(input(f"How many times per year is the interest compounded?:"))
#fTime = float(input(f"How many years will you be leaving your money invested?:"))
#make interest a percentage
#fInterestRate = fInterestRate / 100
#calculate 
#sFutureValue = fPrincipal * (1 + fInterestRate / iComp) ** (iComp * fTime)
#messing around with if statements because why not
#if fTime <= 1:
#    sYearIfMessingAround = "year"
#else:
#    sYearIfMessingAround = "years"
#hope nothing goes wrong in the calculation like a random solar flare flipping an individual bit at the worst time
#print (f"You will have ${sFutureValue :,.2f} at the end of {fTime} {sYearIfMessingAround}.")
print(chr(sum(range(ord(min(str(not())))))))
#Having read through the pdf twice and gthe wikipedia page once the one thing that stuck out to me was i don't quite think you can get a reliable compounding interest of 20% or more outside of a ponzi scheme
#and anyone promising such a thing is either not a fiduciary and thus has alternate plans for your money or may be into insider trading
#it started out with a def for positive validation and inspiration from an older project and all the random programs i have written down in a notebook
def optimistFlt(prompt):
    while True:
        try:
            if positiveFlt <= 0:
                print("This number must be positive.")
                continue
            return positiveFlt
        #tried running without an except and it didn't turn out well
        except ValueError:
            print("Please enter a valid number!")
#now one for the positive ints  also optimistint sounds funny    "are you an optimist or a pessimist? I'm an optimistint."       
def optimistInt
    while True:
        try:
            positiveInt = int(input(prompt))
            if positiveInt <= 0:
                print("This number must be positive with no .00."
                      continue
                    return positiveInt
                except ValurError:
                    print("You HAVE to put in a positive number here.")

#now you put in the things now with defs
def MainOMain():
    sName = input("What is your name?!")
    fPrincipal = optimistFlt("How much is your initial deposit?:")
    fInterestRate = optimistFlt("What is the interest rate on your deposit (using whole numbers for the percentage)?")
# I say the thing
    iTime = optimitInt("How Many months will you let your interest compound?:") #(no partial months .0035 of a month really?)
    f$Goal = optimistFlt("How much is your savings goal?:") # (no $0 is not a savings goal unless something has gone awry, and if it has using an interest calculator would probably be done in negative integers for debt)
#Change the months into a more floatier rate
    fTime = (fInterestRate / 100) / 12
    
#loops!
    fWhatYaGot = fPrincipal
    months = 1
    while months <= iTime:
        fInterest = fWhatYaGot * fInterestRate
        fWhatYaGot = fPrincipal + fInterest
        print(f"{time:15}${fWhatYaGot:,.2f}")
        months = months + 1
    print (f"Your balance after {iTime} months is: ${fWhatYaGot,.2f}")

#goal keeping
    if f$Goal > 0:
        fWhatYaGot = fPrincipal
        ftimefUntilfGoal = 0
#I just think f in front of variables makes them inherently funnier        
        while fWhatYaGot < f$Goal:
            fInterest = fWhatYaGot * fTime
            fWhatYaGot = fWhatYaGot + fInterest
            ftimefUntilfGoal = ftimefUntilfGoal + 1
         print(f"It will take you {ftimefUntilfGoal:,} months to reach your lofty goal of ${f$Goal:,.2f}!")
        else:
            print("No ${f$Goal:,.2f} is not a goal to aspire to! CANCEL YOUR CREDIT CARDS!")
MainOMain()
            
        
