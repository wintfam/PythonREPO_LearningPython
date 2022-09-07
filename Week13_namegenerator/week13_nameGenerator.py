#week 13 Project

#Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
#Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:

#1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
#2. Allow the user to input the name of their department that is used in the unique name.
#3. Generate random characters and numbers that will be included in the unique name.

print("Anthony Wint")
print("Week13 LUIT Project")

print ("Initialize EC2 Random Name Generator")

import random
import string


# List of departments sharing AWS environment

dept_list = ['UX/Design', 'DevOps', 'Software']


# Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
# Allow the user to input the name of their department that is used in the unique name

instance_num = int(input("How many instances are desired? "))
dept = str(input("Enter department name: "))


# Generate random characters and numbers that will be included in the unique name

characters_numbers = (string.ascii_letters + string.digits)
unique_name = ''.join(random.sample(characters_numbers, 8))
print(unique_name)


# Random generated department and EC2 with a unique name

output = (dept_list)
ec2_name = (unique_name)
print(random.choice(dept_list), unique_name)