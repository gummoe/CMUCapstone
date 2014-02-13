"""This is the script for loading the file contents"""

import Address

#Load the file
file_in = open("addresses.txt")

#Create Node list
NodeList = []

#Iterate through the file contents line by line, make a node object, and add to the node
#array
for line in file_in:
	tmp = Address(str(line))
	NodeList.append(tmp)
	print tmp.name

#Close the file when done
file_in.close()
