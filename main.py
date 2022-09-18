#Triangle Verifier
#Create a program that verifies the type of triangle, from the 3 side lengths input by the user.
#Kevin Patel
#October 13, 2021

#Variables
side_Length_One = 0.00
side_Length_Two = 0.00
side_Length_Three = 0.00
x = 0 #place holder


#Variables with User Input and Avoiding Error Input from User
#While x is equal to 0, keep trying to get a valid float or integer value from user. If valid positive number is given then x will equal 1 which will then break the while loop and continue to the next part of the program. If user does not enter correct value then it will continue to ask the user for a valid number.
while (x==0): 
	try:
		#Insert the first side length into the variable called side_Length_One
		side_Length_One = float(input("____________________________________\nPlease Enter The First Side Length\n= ")) 
		#If and else statement to only take postive values from user
		if (side_Length_One > 0): 
			x = 1
		else:
			print("\nPlease input valid number...") 

	except ValueError:
		print("\nPlease input valid number...") 

#While x is equal to 1 from before, keep trying to get a valid float or integer value from user. If valid positive number is given then x will equal 2 which will then break the while loop and continue to the next part of the program. If user does not enter correct value then it will continue to ask the user for a valid number.
while (x==1):
	try:
		#Insert the second side length into the variable called side_Length_Two
		side_Length_Two = float(input("____________________________________\nPlease Enter The Second Side Length\n= ")) 
		#If and else statement to only take postive values from user
		if (side_Length_Two > 0): 
			x = 2
		else:
			print("\nPlease input valid number...") 

	except ValueError:
		print("Please input valid number...") 

#While x is equal to 2, keep trying to get a valid float or integer value from user. If valid positive number is given then x will equal 3 which will then break the while loop and continue to the next part of the program. If user does not enter correct value then it will continue to ask the user for a valid number.
while (x==2):
	try:
		#Insert the third side length into the variable called side_Length_Three
		side_Length_Three = float(input("____________________________________\nPlease Enter The Third Side Length\n= ")) 
		#If and else statement to only take postive values from user
		if (side_Length_Three > 0):
			x = 3
		else:
			print("\nPlease input valid number...") 	
	
	except ValueError:
		print("Please input valid number...") 


#Main Program

#If One side is greater than or equal to the other two sides added together, tell the user that this is not a triangle.
if side_Length_One >= (side_Length_Two + side_Length_Three) or side_Length_Two >= (side_Length_One + side_Length_Three) or side_Length_Three >= (side_Length_One + side_Length_Two):
	print("This is not a Triangle.")

#Else if all three side lengths are the same, tell the user that the triangle is an Equilateral Triangle.
elif side_Length_One == side_Length_Two == side_Length_Three: 
	print("This is an Equilateral Triangle.")

#Else if exactly two triangles are the same length, tell the user that the triangle is an Isosceles Triangle.
elif side_Length_One == side_Length_Two or side_Length_One == side_Length_Three or side_Length_Two == side_Length_Three: 
	print("this is an Isosceles Triangle.")

#Else if all three side lengths are different then tell the user that the triangle is an Scalene Triangle.
elif side_Length_One != side_Length_Two != side_Length_Three: 
	print("This is a Scalene Triangle.")