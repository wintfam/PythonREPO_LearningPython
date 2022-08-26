print ("Hello, World!!")
print ("Week12, Project!!!")


#The list should be empty initially
MyAWSlist = []
print ("n\Emptylist")
print ("MyAWSlist")

#Populate the list using append or insert
MyAWSlist.append("EC2")
MyAWSlist.append("Lambda")
MyAWSlist.append("Cloud9")
MyAWSlist.append("S3")
MyAWSlist.append("DynamoDB")
print ('MyAWSlist')


#Print the list and the length of the list
print ("\nThis prints out the length of our list:")
print ("MyAWSlist")
print (len("MyAWSlist"))

#Remove two specific services from the list

MyAWSlist.remove("EC2")
MyAWSlist.remove("S3")
print ("MyAWSlist")

#Print the new list and the new length of the list
