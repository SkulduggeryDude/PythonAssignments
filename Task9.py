#Functon to take data from external file and format for display.
def read_data(filename):
	#Empty list made for file data to be added
	records = []
	#File to be opened is given in function parameters
	with open(filename) as fr:
		#Taking each line of the file and using .strip to remove all spaces and commas
		lines = fr.readlines()
		for line in lines:
			line = line.strip()
			if len(line) == 0:
				continue
			#With our lines now a list we can set each entry to a variable and add it to our record list.
			str_rec = line.split(",")
			company_name = str_rec[0].strip()
			industry = str_rec[1].strip()
			year_revenue = int(str_rec[2].strip())
			revenue_growth = float(str_rec[3].strip())
			#clean data is added to the list and returned when called
			rec = [company_name, industry, year_revenue, revenue_growth]
			records.append(rec)
	return records

#Function to take the new list and write it to a file
def write_data(filename, data): #filename is what the new file will be named and data is the list to be written to it
	with open(filename, "w") as fw:
		for rec in data:
			fw.write(f"{rec[0]},{rec[1]},{rec[2]},{rec[3]}\n")
			#For each line in our list, write each variable separated by a comma

#Function prints and formats the list to the console
def print_all_records(data):
	#Header printed as f string :>x to space out the text
	print(f"{'Company':>12} {'Industry':>20} {'Revenue (Bn$)':>29} {'Growth':>10}")
	print("-"*75)
	#Index to create a numbered list on the left side
	index = 0
	for rec in data:
		index += 1
		#For loop prints each line as f string to console with :<x to space text
		print(f"{index:<5}{rec[0]:<20}{rec[1]:<25}{rec[2]:<18}{rec[3]:<20}")
	print("\n")

#Function to find lowest revenue in list
def get_min_revenue_record(data):
	#sets current lowest value as the first revenue in the list
	lowest = data[0][2]
	#For loop goes through the list and compares the current value to the lowest variable
	for rec in data:
		compare = rec[2]
		#If the newest record is lower than the lowest, it makes it the new lowest variable to be compared to the rest of the list. 
		if compare < lowest:
			lowest = compare
			#Assigns the entire list to lowest_record, to be returned as the record with the lowest revenue
			lowest_record = rec
	return lowest_record


#function to count the amount of lists with a positive growth
def count_positive_growth_companies(data):
	#sets variable to count companies
	total_positive_growth = 0
	#For loop goes through each list and see if the growth variable is greater than 0, if so it adds 1 to count
	for rec in data:
		if rec[3] > 0:
			total_positive_growth += 1
	#Returns amount of positive growth companies
	return total_positive_growth
			


#Function to print data of a certain industry
def query_revenue_by_industry(data):
	#Asks user for input and assigns to name. Stat variables defined
	name = input("Enter an industry name: ")
	total_revenue = 0
	avg = 0
	rec_count = 0
	#Searches through the records to find matching industry name to user input
	for rec in data:
		#.lower() makes all lowercase to remove case sensitivity error
		if name.lower() == rec[1].lower():
			#Adds revenue to the total
			total_revenue += rec[2]
			#Counts amount of entries to later divide to find average
			rec_count += 1

	#Error checks that data isnt empty and we dont divide by 0 if no industries found
	if len(data) > 0 and rec_count > 0:
		#Average calculated and printed to console to 2 decimals
		avg = total_revenue/rec_count
		print(f"Average revenue: ${avg:.2f}")

	#If the user doesnt enter a matching industry, rec_count wont be added to, so prints error message
	if rec_count == 0:
		print(f"No matching product for {name}")
	#If industry is found then it prints its total revenue
	else:
		print(f"Total revenue: {total_revenue}")
		


#Function to call our other functions
def main():
	#records is set to hold data from our read file function for our functions to use
	records = read_data("data.txt")
	#Writes records to a file
	write_data("backup.txt", records) 
	#Prints and formats records to the console
	print_all_records(records)
	#Lowest record is set to min_record then printed to console as fstrings
	min_record = get_min_revenue_record(records) 
	print(f"The minimum revenue figure is: {min_record[2]}") 
	print(f"Company name: {min_record[0]}\n") 
	#Prints number of companies with positive growth to console as fstring
	print(f"Number of positive growth companies: {count_positive_growth_companies(records)}\n")
	#asks user for industry and prints its stats to console
	query_revenue_by_industry(records) 

#Calls main function to start program.
main()
