#PRINTING STRINGS: Long string, use a triple quote (single or double) 
#to start your string and the same triple quote to end it 

#\n Newline or \t Tab

#Escape characters: \\ Literal Backslash, \" literal double quote" 
#, \'Literal Single Quote' 

"""Event Name \t \t \t Date\\Time \n Happy Hour \t \t \t 7/21,6:00 pm \n Jane's House Party \t \t \t 7/22, 8:00 pm"""

#VARIABLES: variables need to start with a letter, cannot have spaces 

#first_name = "Rachel"
print first_name
#Rachel
#last_name = "Gutauskas" 
print last_name, ",", first_name 
#Gutauskas , Rachel
print last_name,",",first_name
#Gutauskas , Rachel

#SLICING: first_name[0], 0 is the index that you want to see
print first_name[1:5]
#ache
print first_name[:5]
#Rache
print first_name[0:]
#Rachel 

#STRINGS: 
print "My name is: {0} and my age is: {1}".format(first_name,age)
#curly bracket is a placeholder for an upcoming variable 
#.format is used only for strings, put variables in to the placeholders
#'My name is: Rachel and my age is: 24'
print "My name is {0} and my age is {1:,}".format(first_name,age)
#separates the age value with commas 

phone_number = "2025559876"
#print phone number
print "My number is {0}".format(phone_number)
#local number
print "My local number is {0}".format(phone_number[3:])
#domestic number 
print "My domestic number is ({0}){1}-{2}".format(phone_number[0:3],phone_number[3:6],phone_number[6:])
#My domestic number is (202)555-9876
#international number 
print "My international number is +1-{0}-{1}-{2}".format(phone_number[0:3],phone_number[3:6],phone_number[6:])
#My international number is +1-202-555-9876

#STRING METHODS: let you perform special actions on your strings 
.find
email_address = "rachel@gutauskas.com"
email_address.find("@")
#will calculate where it found that variable 
# if it doesn't find it, it returns -1
email_address.find("0")

.replace
phone_number = "202-555-1234"
#want to change the last 4 digits
phone_number = phone_number.replace("1234", "1245")
print phone_number

len()
#prints the length of the string or the list

#ARGUMENTS: are what you give to a function or a method(action)
grocery_list = "apples,oranges,pears"
length = len(grocery_list)
print length
>>>20

.strip() #take out the white space at the beginning or end of a string
.lower() #turns everything lowercase
.upper() #turns everything upper case
.count() #how many times a string appears 

#CONDITIONALS: yes or no question, way to compare things and use that information to make decisions 
#can let you change the behavior of the program 
#conditionals are paired with if statements, ask whether or not a condition is true 
# use : as a stop point of a condition 

if fundraising >= goal:
	print "Congrats!"

#conditional statement using an else if 
if age >= 21:
	print "you're old enough to drink"
elif 21 > age >=18:
	print "you're old enough to vote but not old enough to drink"
else:
	print "you're too young to be in this bar!"

#OPERATORS: the ways to compare things 
== #equality operator, used for testing two variables 
5==7
False
5==5
True 

#use upper and lower to make operator case insensitive 
first_name = "Rachel"
name = "RACHEL"
first_name.lower() == name.lower()
True

#CONDITIONALS
volunteer_goal = 100
current_volunteers = 50
if current_volunteers >= volunteer_goal:
	print "Great job!"
elif current_volunteers == volunteer_goal:
	print "You've met your goal"
else:
	print "Gotta get more volunteers!"


#COMPOUND CONDITIONALS: 
if email_address.count("@") >1:
	print "not a valid email address"
