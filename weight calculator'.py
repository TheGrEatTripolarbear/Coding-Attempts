#this is for their name
sName = input(f"What is your name?:")
#this is for their weight
earthWeight = float(input(f"How much do you weigh?:"))
#this is the calculations

mercuryWeight = (earthWeight*(0.38))
venusWeight = (earthWeight*(0.91))
moonWeight = (earthWeight*(0.165))
marsWeight =  (earthWeight*(0.39))
jupiterWeight = (earthWeight*(2.34))
saturnWeight = (earthWeight*(0.93))
uranusWeight = (earthWeight*(0.92))
neptuneWeight = (earthWeight*(1.12))
plutoWeight = (earthWeight*(0.066))
#This is where the things are returned
print(f"This is your weight on earth {sName:<17} {earthWeight :>10.2f}")
print(f"This is your weight on mercury {sName:<15} {mercuryWeight :>10.2f}")
print(f"This is your weight on Venus {sName:<17} {venusWeight :>10.2f}")
print(f"This is your weight on the moon {sName:<14} {moonWeight :>10.2f}")
print(f"This is your weight on Mars {sName:<18} {marsWeight :>10.2f}")
print(f"This is your weight on Jupiter {sName:<15} {jupiterWeight :>10.2f}")
print(f"This is your weight on Saturn {sName:<16} {saturnWeight :>10.2f}")
print(f"This is your weight on Uranus {sName:<16} {uranusWeight :>10.2f}")
print(f"This is your weight on Neptune {sName:<15} {neptuneWeight :>10.2f}")
print(f"This is your weight on Pluto {sName:<17} {plutoWeight :>10.2f}")

