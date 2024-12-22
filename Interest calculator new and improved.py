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
#and anyone promising such a thing is either not a fiduciary and thus has
#alternate plans for your money
#or may be into insider trading
#it started out with a def for positive validation and inspiration from an
#older project and all the random programs i have written down in a notebook
def optimistFlt(prompt):
    while True:
        try:
            positiveFlt = float(input(prompt))
            if positiveFlt <= 0:
                print("This number must be positive.")
                continue
            return positiveFlt
        #tried running without an except and it didn't turn out well
        except ValueError:
            print("Please enter a valid number!")
#now one for the positive ints  also optimistint sounds funny
#"are you an optimist or a pessimist? I'm an optimistint."       
def optimistInt(prompt):
    while True:
        try:
            positiveInt = int(input(prompt))
            if positiveInt <= 0:
                print("This number must be positive with no decimals.")
                continue
            return positiveInt
        except ValueError:
             print("You HAVE to put in a positive number here.")

#now you put in the things now with defs
def MainOMain():
    sName = input("What is your name?!")
    fPrincipal = optimistFlt("How much is your initial deposit?:")
    fInterestRate = optimistFlt("What is the interest rate on your deposit?")
# I say the thing
    iTime = optimistInt("How Many months will you let your interest compound?:")
    fGoal = optimistFlt("How much is your savings goal?:") # (no $0 is not a savings goal unless something has gone awry, and if it has using an interest calculator would probably be done in negative integers for debt)
#Change the months into a more floatier rate
    fTime = (fInterestRate / 100) / 12
    
#loops!
    fWhatYaGot = fPrincipal
    months = 1
    while months <= iTime:
        fInterest = fWhatYaGot * fTime
        fWhatYaGot = fWhatYaGot + fInterest
        print(f" months{months:3} and money ${fWhatYaGot:,.2f}")
        months = months + 1
    print (f"Your balance after {iTime} months is: ${fWhatYaGot:,.2f}")

#goal keeping
    if fGoal > 0:
        fWhatYaGot = fPrincipal
        ftimefUntilfGoal = 0
        # fI fjust fthink ff fin ffront fof fvariables fmakes fthem finherently ffunnier
        while fWhatYaGot < fGoal:
            fInterest = fWhatYaGot * fTime
            fWhatYaGot = fWhatYaGot + fInterest
            ftimefUntilfGoal = ftimefUntilfGoal + 1
        print(f"{sName} it will take you {ftimefUntilfGoal:,} months to reach your lofty goal of ${fGoal:,.2f}!")
    else:
        print(f"No ${fGoal:,.2f} is not a goal to aspire to! CANCEL YOUR CREDIT CARDS!")

MainOMain()
#Also i'm thinking of trying to write a program to help organize
#a music festival if I find some spare time should i start with what
#i currently know or should I wait till python 2? According to the organizer
#they use 3 seperate programs to try and get it organized and its a bit of a
#headache. But also they are professional programs from companies so i'm uncertain of
#whether a "fun" side project would in fact be better
            
        
