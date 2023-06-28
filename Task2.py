#Program for calculating the dimensions of a rectangle

print("Find the dimentions of a rectangle \nPlease enter a number, e.g. 9.5\n")

#Takes user input as a float and assigns it to variables width and height
width = float(input("Enter width of rectangle: "))
height = float(input("Enter height of rectangle: "))

#Caculating area and perimeter with our variables
area = width * height
perimeter = (width + height) * 2

#prints output to console
print("")
print("Perimeter:",perimeter)
print("Area:",area)
