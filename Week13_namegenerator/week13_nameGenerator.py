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
from time import sleep

#Identify Department/Area
dept = []
dept = input ("UX/Design, DevOps, Audio-Visual, Software\n")
ec2_name= int(len(input("Insert the amount of EC2 instances preferred:")))

num_of_instances = input('How many EC2 instances do you want to provision?\n')

#2. Allow the user to input the name of their department that is used in

department = input('What is your department?\n')

print(f"You have asked to provision {num_of_instances} EC2 instances for the {dept} department\n The names are: \n")

#3.Generate random characters and numbers that will be included in the unique name.
for _ in range (int(ec2_count)):
print (str(dept), ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(N)]))