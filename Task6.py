# Determine first home buyer credit eligibility

#Code loops while asking user for their income, if user input is less than 0 it prints error then will ask again
while True:
  familyAnnualIncome = int(input("Enter family annual income:"))
  if familyAnnualIncome >= 0:
    break
  else:
    print("Invalid input. Try again")

#Code loops while asking user for annual expenses, if user input is less than 0 it will print error then ask again
while True:
  familyAnnualExpense = int(input("Enter family annual expenses: "))
  if familyAnnualExpense >= 0:
    break
  else:
    print("Invalid input. Try again")


#Code asks if user has owned a house with y or n, code makes input uppercase and if its not Y or N then it will print error and ask again
while True:
  previouslyOwnedHouse = str(input("Have you owned a house before? Y/N: ")).upper()
  if previouslyOwnedHouse == "Y" or previouslyOwnedHouse == "N":
    break
  else:
    print("Invalid input. Try again")

#family savings is the income minus the expenses
familyAnnualSavingAmount = familyAnnualIncome - familyAnnualExpense

#prints outputs
print("Family saving amount: " + str(familyAnnualSavingAmount))
print("Previous house ownership: " + previouslyOwnedHouse)

#Code decides if the loan is approved if their savings is higher than 10000 and they havnt owned a house before. prints according output
if familyAnnualSavingAmount >= 10000 and previouslyOwnedHouse == "N":
  print("You are approved for a home loan")
  
else:
  print("Sorry you are not elligable for a home loan")
