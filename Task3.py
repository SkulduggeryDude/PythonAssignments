#Calculates cost of buying timber

#Defines float variables with user inputs
regularTimberPrice = float(input("Enter price for regular: "))
regularTimberMeters = float(input("Enter metres for regular: "))
premiumTimberMeters = float(input("Enter metres for premium: "))

#Calculates the total price of both timbers using our inputs
premiumTimberPrice = regularTimberPrice * 2
regularTimberTotal = regularTimberPrice * regularTimberMeters
premiumTimberTotal = premiumTimberMeters * premiumTimberPrice
allTimberPriceTotal = regularTimberTotal + premiumTimberTotal

#Formats the cost as currency by rounding by two digits with .2f and adding a dollar sign with $. Variables turn from floats into strings by doing this.
regularTimberTotal =  "${:,.2f}".format(regularTimberTotal)
premiumTimberTotal =  "${:,.2f}".format(premiumTimberTotal)
allTimberPriceTotal =  "${:,.2f}".format(allTimberPriceTotal)


#Calcualtes padding of right output by doing 40 spaces minus the length of the text output
regularLength = 40 - len("Regular grade total: ")
premiumLength = 40 - len("Premium grade total: ")
allLength = 40 - len("Total: ")

#Prints totals, adds padding to the left of the cost with the length of the text output
print("\nPayment details: \n")
print(f"Regular grade total:{regularTimberTotal:>{regularLength}}")
print(f"Premium grade total:{premiumTimberTotal:>{premiumLength}}")
print("---------------------------------------")
print(f"Total:{allTimberPriceTotal:>{allLength}}")
