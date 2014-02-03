# Goal #1: Write a new version of the PB&J program that uses a while loop.  
#Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

bread = int(raw_input("How many slices of bread do you have?"))

jelly = int(raw_input("How many spoons of jelly do you have?"))

peanut_butter = int(raw_input("How many spoons of peanut butter do you have?"))

sandwiches = min(bread/2,jelly,peanut_butter)

#print sandwiches

sand_number = range(1,sandwiches+1)
#makes a list of the number of sandwiches we can make (1,2,3,4)

while sandwiches > 0:
	current_sandwich=sand_number.pop(0) 
	sandwiches -= 1
	print "I'm making sandwich #{0}".format(current_sandwich)

