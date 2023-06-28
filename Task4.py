#Display season of the month

#validMonth is a list of accepted inputs for the program
validMonth = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

#Sets user input to string userMonth and makes it lowercase
userMonth = input("Enter the first three letters of a month to see its season: ").lower()

#if the users input is in the valid month list, it will start checking to see which season it is in.
if userMonth in validMonth:

  #userMonth is checked against every month, if one is true then it prints the output string
  if userMonth == "dec" or userMonth == "jan" or userMonth == "feb":
    print("Stinking hot summer")
  
  elif userMonth == "mar" or userMonth == "apr" or userMonth == "may":
    print("Warm colours autumn")

  elif userMonth == "jun" or userMonth == "jul" or userMonth == "aug":
    print("A bit nippy winter")

  elif userMonth == "sep" or userMonth == "oct" or userMonth == "nov":
    print("Super springy spring")
  
  #Else statement if one of our if statements breaks
  else:
    print("Something went wrong")

#if the user doesnt add one of our valid inputs, then it will output an error message and end the program.
else:
  print("ERROR: Please enter the first three letters of a month")
