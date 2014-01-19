# This script will be the basic model of the allergy idea
# Part I: 
	# Show the user past files that have been created. If none, prompt the user to create one.

import os
userdir = raw_input("Please enter the directory name where you store your allergy information:\n\t>")

print ""
print "This is a list of all the Directories and files... "
filestuff = os.listdir(userdir)
print filestuff
print ""

userfile1 = raw_input("Please choose which file you would like to open: ")
userfile2 = open(userfile1,'r')
print userfile2.read()

