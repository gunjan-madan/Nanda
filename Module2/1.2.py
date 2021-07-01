#Lets Learn using multiple conditions


"""-----Task 1:  What is your score? ---------"""
print(" ")
print("*** Task 1: ***")
# Write a program to get the marks for Mathematics from the user. 
# If the marks is less than 50 or equal to 50, print a message saying “you need to improve”.
# If the mark is between 50 and 80, print “ Let's work little more!”
# If the mark is more than 80, print “ You are doing good. Keep it up!”
marks=int(input("Enter your marks:"))
if marks<=50:
  print("You need to improve.")
elif marks>50 and marks<80:
  print("Let's work a little more!")
else:
  print("You're doing good. Keep it up!")
"""-----Task 2:  Which sides are equal? ---------"""
print(" ")
print("*** Task 2: ***")
#In this program we will take three sides of a triangle as input from user
#Compare the sides to check if they are equal
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if (a!=b):
  print("The sides are not equal.")
elif a==c:
  print("The sides are equal.")
else:
  print("The sides are not equal.")