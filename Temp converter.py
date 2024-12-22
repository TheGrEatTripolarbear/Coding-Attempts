#Get temp
fTemp = float(input("Please input the temperature you would like to convert:"))

# ask good questions
sValueSystem = input (f"Is the temperature in celcius (C) or fahrenheit (F):")

while sValueSystem != "C" and sValueSystem != "c" and sValueSystem != "F" and sValueSystem != "f":
     print (f"That is not a supported temperature system, try again!")
     sValueSystem = input (f"Is the temperature in celcius (C) or fahrenheit (F):")
#After much wrestling with multiple and or s I realized I don't know how to end a program early I searched my notes in a panic
#then I figured why not make the correct answer mandatory instead you will put an F,f,C, or c python has all day I don't.    
#calculate with more loops
if sValueSystem == "C" or sValueSystem == "c":
    while fTemp > 100:
        fTemp = float(input("Please use a number lower then boiling point (100) for celsius:"))
if sValueSystem == "C" or sValueSystem == "c":
        fNewTemp = (9/5) * fTemp + 32
        print (f"Your temperature is {fNewTemp :.1f} in fahrenheit or {fTemp :.1f} in celsius.")
#ITS LOOPS ALL THE W(hile)AY DOWN
if sValueSystem == "F" or sValueSystem == "f": 
    while fTemp > 212:
        fTemp = float(input("Please use a number lower then boiling point (212) for fahrenheit:"))
if sValueSystem == "F" or sValueSystem == "f":
        fNewTemp = (5/9) * (fTemp - 32)
        print (f"Your temperature is {fNewTemp :.1f} in celsius or {fTemp :.1f} in farenheit.")
# I know you may be asking yourself why didnt I put the loops in earlier? Mainly a reverse epiphany. Trust me there is no word for reverse epiphany though
#there should be, maybe something like an epiphanope or epiphanone. It's like a feeling of "Have I completely missed the point? Yes I have but how?"
#I beleive A principal in Billy Madison put it best
#"Mr. Madison, what you've just said is one of the most insanely idiotic things I have ever heard.
#At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.
#Everyone in this room is now dumber for having listened to it. I award you no points, and may God have mercy on your soul." Josh Mostel - Principal Max Anderson


