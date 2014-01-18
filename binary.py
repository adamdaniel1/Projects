# This program is made to convert a number to binary

print "Hello World! This program will allow you to convert a number into binary."
print "This program only allows numbers from -255 to 255 as it simulates an 8-bit computer."

while True:
	response1 = raw_input("Please enter 'yes' or 'no' to continue: ")
	if response1 == "yes":
		print "Exciting"
		break
	elif response1 == "no":
		raw_input("CTRL-C to exit the program, or hit ENTER to continue")
		break

# while user does not input a number, it will repeat the print command until user adds a number.

while True:
	usernumber = input("Enter your number: ")
	if -255 <= usernumber <= 255:
		break
	else:
		print "That was not a number, or the number was greater than 255 or less than -255"
		
print "The number you entered was: ", usernumber

#this is were the magic happens
if usernumber >= 128:
	usernumber = usernumber - 128
	print 1
elif usernumber <=128:
	print 0

if usernumber >= 64:
	usernumber = usernumber - 64
	print 1
elif usernumber <= 64:
	print 0

if usernumber >= 32:
	usernumber = usernumber - 32
	print 1
elif usernumber <= 32:
	print 0

if usernumber >= 16:
	usernumber = usernumber - 16
	print 1
elif usernumber <= 16:
	print 0

if usernumber >= 8:
	usernumber = usernumber - 8
	print 1
elif usernumber <= 8:
	print 0
	
if usernumber >= 4:
	usernumber = usernumber - 4
	print 1
elif usernumber <= 4:
	print 0
	
if usernumber >= 2:
	usernumber = usernumber - 2
	print 1
elif usernumber <= 2:
	print 0
	
if usernumber >= 1:
	usernumber = usernumber - 1
	print 1
elif usernumber <= 1:
	print 0
	
while 0 != usernumber < 1:
	usernumber * 2
	print 0
	if usernumber >= 1:
		usernumber - 1
		print 1
print "Done!"

exit()
# Created by Adam Daniel. Last Updated January 14th, 2014.
"""
Things left to do: 		Make negative numbers work
						Make numbers < 1 work
						Make while loop in (line 17) not crash if user inserts a string.
"""