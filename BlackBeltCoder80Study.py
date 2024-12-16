if 7 > 5: # This is Module 2: Python Basics. 
    #Lesson 1: Python Syntax

    #This is a print
    print("Seven is greater than five!")
    
    # This is a comment
    print ("this is a comment!")

    #This is a print
    print( 'this is not a comment')

    #This is my variable
    a = "hi!"

    #This is a conditon 
    if 9 > 5:
        print("a")
        # Triple Multi-line quotes creats a document like format like for writing paragraphs
    a = '''Python's 
    Multi-line
    groove'''
# Backward slash creates space between code like for a document.
    b = "Hello, Coding Temple \
    How are you today?"

print(a)
print(b)
# Multi-line exaple. print(a) is needed to print code out in terminal
a = '''My Hobby is doing martial arts.
    I find it relaxing and enjoyable!'''
print(a)

# Adding numbers
print(12+12)

#Another method of coding intergers for adding.
sum = 5+3
print("the sum of 5 and 3 is:",sum)

#M Module 2: Python Basics Topic:2 Documentation: Your Gateway to Python Mastery

# A. Basic Variables:
# Question = What is a Variable in Python?
# Answer = Variables are essentially names assigned to values or reference to values stored in memory. Variable allow
# you to store, modify, and retrieve data while your program is running (during the execution of your Python code).
# Example.
Car = "Four wheeled vehicle"
print(Car)
# The word "Car" is a variable. "Four wheeled vehicle" is a Value.
# Question = How is memory allocated for variables done?
# Answers = Variables are assigned values which are created as objects in memory to store the value.
# These values act as reference. Here is a personal breakdown of Memory allocation.
# Stack Memory, Variable are stored in stack memory. Which keeps track of active variables and any assocaited values stored
# in them. 
# Heap Memory Stores something like the actual data ("strings, integers, list ect."). Is used to Deallocation of memory.
# Garbage Collection is described as Automatic memory managment (AMM). 
# Example = This is behind the seen but active contantly.

# B. Variable Assignment:
# Question = Explore how to assign values to variables
# Answer = Car is a Variable. That is assigned a value of "Four wheeled vehicle".
# Example.
Plan = "Metal flying Machine"
print(Plan)
# Question Can a variable hold multiple values?
# Answer = Yes
# Example.
Lavon = "AAPEX Business Partner and is our CMO", "she is 41 not", ["42,43,44,45"]
print(Lavon)
# Lavon = Variable
# AAPEX Business Partner and is our CMO etc. = Tuple
# 42, 43, 44, 45 = List str

# C. Variable Naming Conventions
# Question = Research the rules and conventions for naming varibles.
# Answer= Variable naming conventions are  basically guidlines.
# These guidlines are used to help developers better name variables. That hint at its purpose within the code.
# some names are reserved and cannot be used as variables. Examples are: (e.g., for, if, class, def, etc).
# Also some python is case sensitive. So Leroy is different form leroy. SW programers are encourgaged to use.
# Case Stles for Variables (Snake Case, and Camel Case,). 
# Example.
First_Generation = "Leroy Tillman I"
Second_Generation = "Leroy Tillan II"
Third_Generation = "Leroy Tillman III"
Fourth_Generation = "Leroy Alexander Tillman IV" 
Generation = "These are four Generations of The House of Lions over 100 ye of tradition"
print(First_Generation)
print(Second_Generation)
print(Third_Generation)
print(Fourth_Generation)
print(Generation)
# These are all example of conventions for naming variables.
# Question = Identify a list of reversed keywords that cant be used as variable names.
# Answer = some example are on line 79 above.

# Dynamic Typing:
# Question = How does Python Handle Variable types?
# Answer = Variable types or changed by its values. However a variable is an object. Variables are references to types.
# Example.
# the first part is the variable the second is its type (value)
variable = "type"
print(variable)
vtype = "values"
print(vtype)
# Question = Look into how a variable's type can change during runtime.
# Answer = Variables can change during run time due to reassignment of values types.
# Example.
x = 5
print(x) # interger
x = 0.5 # float
print(x)

# E. Multiple Assigments:
# Question = Can you assing values to multiple variables in a single line? Discover How.
# Answer = Yes you can do this by seperating them with commas on a single line
# Single.
#Example.
LT1 = LT2 = LT3 = LT4 = "All Four Generations" # All the Variables equal All Four Generations
print(LT1)
print(LT2)
print(LT3)
print(LT4)
LT1, LT2, LT3 = 1, 2, 3
print(LT1)
print(LT2)
print(LT3)
# cookies example for video
cookies = 10 
print(cookies) # this will output 10
# Code Example 
print ("Hello, Alex!")
# With Variables:
user_name = input ("Whats your name?")
print ("Hello," + user_name + "!")
# My Personal Code will ask name and age and say something like okay to the user.
user_age = input ("Whats your age")
print ("So, your age is" + user_age + "?")
response = input("Want to play a game," + user_name + "\U0001F608" "? (yes/no): ")
if response.lower() == "yes":
    print("Great!" + user_name +" this is going to change your life FOREVER...!!!")
else:
    print("Too bad" + user_name +" THE GAME STARTED THE VERY MOMENT YOU LOGGED IN")
# Case Type to remember for variables
# camel_Case
# snake_case
# Pascal_Case

#Data Type
# Text type (str)
beach ="Sunny Shore"
print(beach)
# Numeric Types (int, floats, complex)
waves_today = 5 # this is an interger
tide_height = 3.4 # This is float
print(waves_today)
print(tide_height)
# Literal Values: True (capital T) and False (capital F). They are distinct form the strings "True" and "False".
#Booleans (bool) USed for if statments or in need of a clear binary (yes.no, true/false. on/off)
is_sunny = True
is_raining = False
print(is_sunny)
print(is_raining)
#amount = 100
#print(type(amount)) # Output: <class 'int'> I could not get this function to work.
user_print = input("Enter a number")
print(type(user_print)) 
x = "123"
print(type(x))
y = int (x) 
print(type(y))

#Dynamic Typing-Python's Superpower
my_variable = "Hello, World"
print(my_variable) # Outputs Hello, World!
print(cookies)

# Video Follow Along
# Define two variable: myName and myname. Assign your first name to myName and your last name to myname.
# Print both variables: Is the output what you expected?
# Assign your favorite color to a variable called fav_color and print it.

myName = "Leroy"
myname = "Tillman"
print(myName, myname)

fav_color = "Oragne"
print(fav_color)

# Assign values "apple", "banana", and "cherry" to variables fruit1, fruit2, and fruit3 in a single line.
# Print all three nariables.

fruit1, fruit2, fruit3 = "apple", "banana", "cherry"
print(fruit1,fruit2,fruit3)

# Assign an interger, a float, and a string to three different variables
# Print each variable and its type using the type() function.

math1 = 1
division = 4.5
words = "house"
print(math1, division, words)
print(type(math1))
print(type(division))
print(type(words))

# Given the variable mystery_variable = "1234". use the type() function to determine its data type.

mystery_variable = "1234"
print(mystery_variable)
print(type(mystery_variable))
# Assign a numnber to a variable named dynamicVar. Now, reassign a string value to dynamicVar.
# Print the variable and its type after each assignment

dynamicVar = 1
print(dynamicVar)
print(type(dynamicVar))
dynamicVar = "Leroy likes bananas"
print(dynamicVar)
print(type(dynamicVar))
# Write a short script that tries to use if as a variable name. What error do you get
#if = "Dog" #SyntaxError

# Assign multiple values to multiple variables.
my_Var1, my_Var2, my_Var3 = "Leroy will be",  (user_age) + " years old coming", 2025

# Print the type of each variable
print(type(my_Var1))
print(type(my_Var2))
print(type(my_Var3))
print(my_Var1, my_Var2, my_Var3)

# Use a keyword as a variable name to observe the kind of error Python throws.
#while = 5
#print(while) #SyntaxError


