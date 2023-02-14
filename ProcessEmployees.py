"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file
employee = open("employee_data.csv", "r")
employee_details = csv.reader(employee, delimiter=",")
next(employee_details)


# create an empty dictionary
employee_reward = {}

# use a loop to iterate through the csv file
for record in employee_details:
    # print('ID', record[0])

    # check if the employee fits the search criteria
    if record[9] == "TS":
        salary = int(record[5])
        bonus = 0.1 * salary
        new_salary = bonus + salary
        # print(salary, new_salary)

        employee_reward[record[0]] = {}
        employee_reward[record[0]]["Full name"] = record[1] + " " + record[2]
        employee_reward[record[0]]["New Salary"] = new_salary
    print(f'Employee Name: {record[1] + " " + record[2]} Current salary: {record[5]} ')


print(f'Employee Name: {record[1] + " " + record[2]} Current salary: {record[5]} ')

print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image
for each in employee_reward:
    print(
        f"Employee Name: {employee_reward[each]['Full name']} New salary {employee_reward[each]['New Salary']}"
    )


print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.

print()


employee.close()
