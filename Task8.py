def get_records():
	# Compose a list of course records
	# Record format: course id, title, enrolment number, and pass student number
	course_list = []
	course_list.append(['COMP001', 'Fundamentals', 135, 126])
	course_list.append(['COMP002', 'Database Principles', 30, 28])
	course_list.append(['COMP003', 'Networking', 24, 22])
	course_list.append(['COMP004', 'Website Development', 45, 41])
	course_list.append(['COMP005', 'IT Support', 50, 48])
	return course_list

def display_list(records):
	#Printing header using f string :<10 to print blank space
	print(f"{'ID':<10}{'Course':<25}{'Passed':<10}{'Students':<10}")
	print("-"*55)

	#Loop for printing each line in the list. Prints the second, third and forth entry in every list and adds blank spaces using the f strng.
	for i in get_records():
		print(f"{i[0]:<10}{i[1]:<25}{i[3]:<10}{i[2]:<10}")

	#Prints a blank line then the amount of courses in the list
	print("\nCourse count:", len(get_records()),"\n")


def search_by_course_id(data):
	# write code for the function
	# Note, the function is none-value-return function
	#Function parameter is set to user input and made uppercase to match list values
	search = input("Enter course code: ").upper()
	#Set variable searchFound to False, will be assigned True if search is found in list
	searchFound = False
	#Goes through all the records, if the search matches the ID then it prints the total students minus the passed
	for i in data:
		if i[0] == search: 
			print("Course matching given ID:",i[1])
			print("Number of students who didn't pass:",i[2] - i[3])
			#Sets searchfound to True so the if statement below wont execute
			searchFound = True
			break
	#If the if statement doesnt get passed to make searchFound True it prints an error message, then continues to the next function
	if searchFound == False:
		print("Course not found\n")

def get_total_fail(data):
	# write code for the function
	# Note, the function is value-return function
	total_fail = 0
	#Code goes through each list and adds the number of students, minus the number that passed to total_fails
	for i in data:
		total_fail += i[2] - i[3]
	#Returns function call with interger assigned to total_fail
	return total_fail

def main():
	rec_list = get_records()
	display_list(rec_list)
	#complete the call of search_by_course_id function here
	#Hint: the function is none-value-return function
	search_by_course_id(rec_list)
	#complete the call of get_total_fail function here
	#Hint: the function is value-return function
	#get_total_fail is called as a variable that returns an integer
	print("\nTotal number of students who didn't pass:", get_total_fail(rec_list))

main()
