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


#Identify Department/Area

ec2_name = int(input("Insert the amount of EC2 instances preferred:"))

num_of_instances = input(int('How many EC2 instances do you want to provision?'))

#2. Allow the user to input the name of their department that is used in

department = input('What is your department?')

print(f"You have asked to provision {num_of_instances} EC2 instances for the {department} department")

#3.Generate random characters and numbers that will be included in the unique name.
counter = 1
allowed = ['UX/design' , 'Devopps' , 'Software' , 'Scrum Master']

how_many = int(input("number of EC2 will be created?"))
dept = input("name your department")

if dept not in allowed
    print('This genarator is restricted to specific department only!!!')
    
else:
    while counter <= how_many:
        letter = random.choices(string.ascli_letters, k=3)
        letterlist = "" .join(letters)
        numbers = random.sample(range(100, 999), k=1)
        print(dept.title()+"-"+letterlist+str(*numbers))
        counter += 1