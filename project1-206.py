import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


###	GIT HUB ACCOUNT INFORMATION###
### LINK TO GITHUB:





def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
#read all the lines and close the file

	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()

	#init list of dictionary items
	list_dict = []

	#loop through the lines and get a list of dictionaries
	for line in lines:

		#creating a new dictionary for the values in this line
		data_dict = {}
		values = line.strip().split(',')

		first_name = values[0]
		last_name = values[1]
		email = values[2]
		class_year = values[3]
		dob = values[4]

		#setting up the dictionary
		data_dict["First"] = first_name
		data_dict["Last"] = last_name
		data_dict["Email"] = email
		data_dict["Class"] = class_year
		data_dict["DOB"] = dob

		list_dict.append(data_dict)

	return list_dict

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sortedList = sorted(data, key = lambda z: z[col])

	return sortedList[0]["First"] + " " + sortedList[0]["Last"]


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#class init counters
	num_fresh = 0
	num_soph = 0
	num_junior = 0
	num_senior = 0

	for d in data:
		if d["Class"] == "Freshman":
			num_fresh += 1

		elif d["Class"] == "Sophomore":
			num_soph += 1

		elif d["Class"] == "Junior":
			num_junior += 1

		elif d["Class"] == "Senior":
			num_senior += 1

	tup_list_students = [("Freshman", num_fresh), ("Sophomore", num_soph), ("Junior", num_junior), ("Senior", num_senior)]

	sorted_TList = sorted(tup_list_students, key = lambda z: z[1], reverse = True)

	return sorted_TList


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

    birth_months = {}

    for z in a:

        m = z["DOB"].split('/')[0]

        if m not in birth_months:
            birth_months[m] = 0
        else:
            birth_months[m] += 1

    sortedMonthList = sorted(birth_months.items(), key = lambda z: z[1], reverse = True)

    return int(sortedMonthList[0][0])




def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	outFile = open(fileName, "w")

	sortedFile = sorted(a, key = lambda z: z[col])

	for x in sortedFile:

		outFile.write(x["First"] + "," + x["Last"] + "," + x["Email"] + "\n")

	outFile.close()

	return


def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass







################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
