#Program for printing list of student pass rates for each course
#Compose a list of course records
course_list = []
course_list.append(['COMP001', 'Fundamentals', 135, 126])
course_list.append(['COMP002', 'Database Principles', 30, 28])
course_list.append(['COMP003', 'Networking', 24, 22])
course_list.append(['COMP004', 'Website Development', 45, 41])
course_list.append(['COMP005', 'IT Support', 50, 48])

#Printing header using f string :<10 to print blank space
print(f"{'Course':<25}{'Passed':<10}{'Students':<10}")
print("-"*45)


#Loop for printing each line in the list. Prints the second, third and forth entry in every list and adds blank spaces using the f strng.
for i in course_list:
	print(f"{i[1]:<25}{i[3]:<10}{i[2]:<10}")

#Prints a blank line then the amount of courses in the list
print("\nCourse count:", len(course_list))
