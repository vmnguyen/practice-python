#!/usr/bin/python3

# Get a number from user,
num = int(input("Give me a number: "))
check = int(input("Give me a check number: "))
# Check if check is devided evenly to num
if check % num == 0:
	print ("The check number is devides evenly to num")
else:
	# Check whether input is odd or even
	if num % 2 == 0:
		# Check if num is devided to 4
		if num % 4 == 0:
			print ("The number you just entered is Mutilple of 4")
		else:
			print ("The number you just entered is Odd")
	else: 
		print ("The number you just entered is Even")