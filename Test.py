#Return Functon to take data from external file and format for display.
def read_data(filename):
	#Empty list made for file data to be added
	student_records = []
	#File to be opened is given in function parameters
	with open(filename) as fr:
		#Taking each line of the file and using .strip to remove all spaces and commas
		lines = fr.readlines()
		for line in lines:
			line = line.strip()
			if len(line) == 0:
				continue
			#With our lines now a list we can set each entry to a variable and add it to our record list.
			stu_rec = line.split(",")
			student_id = stu_rec[0].strip()
			student_name = stu_rec[1].strip()
			student_grade = float(stu_rec[2].strip())
			#clean data is added to the list and returned when called
			rec = [student_id, student_name, student_grade]
			student_records.append(rec)
	return student_records

#Non-return function to find and print certain record
def search_student_by_id(records):
	#Function parameter is set to user input and made uppercase to match list values
	search = input("Enter student ID: ").upper()
	#Set variable searchFound to False, will be assigned True if search is found in list
	searchFound = False
	#Goes through all the records, if the search matches the ID then it prints the students name and grade
	for rec in records:
		if rec[0] == search: 
			print("Student matching given ID:",rec[0],rec[1])
			print("Student grade:", rec[2],"\n")
			#Sets searchfound to True so the if statement below wont execute
			searchFound = True
			break
	#If the if statement doesnt get passed to make searchFound True it prints an error message, then continues to the next function
	if searchFound == False:
		print("Student not found\n")

#Non-return function calculates and displays the average grade of all students
def calc_average_grade(records):
	average = 0
	count = 0
	#For loop goes through every record, counting each record and totaling every grade
	for rec in records:
		average += rec[2]
		count += 1
	#Average calculated by dividing total by count of entries in the list
	average = average/count
	#Prints with f string to two decimal places
	print(f"The average grade of all students is: {average:.2f}")

#Non-return function calculates and displays total passed and failed
def calc_grade_stats(records):
	total = 0
	count_passed = 0
	#For loop counts every record in list and counts if the grade was passing(50 or more)
	for rec in records:
		total += 1
		if rec[2] >= 50:
			count_passed += 1
	#Prints passed amount and prints failed with the total students minus the ones who passed to get the leftover failed
	print(f"The number of students who have passed: {count_passed}")
	print(f"The number of students who have failed: {total-count_passed}")


#Return function to find lowest grade in list
def get_min_grade(records):
	#sets current lowest value as the first grade in the list
	lowest = records[0][2]
	#For loop goes through the list and compares the current grade to the lowest grade
	for rec in records:
		compare = rec[2]
		#If the newest record is lower than the lowest, it makes it the new lowest variable to be compared to the rest of the list. 
		if compare < lowest:
			lowest = compare
			#Assigns the entire list to lowest_record, to be returned as the record with the lowest grade
			lowest_record = rec
	return lowest_record


def main():
	records = read_data("student_data.txt")
	search_student_by_id(records)
	calc_average_grade(records)
	calc_grade_stats(records)
	print(f"The lowest grade is: {get_min_grade(records)[2]}")

main()
