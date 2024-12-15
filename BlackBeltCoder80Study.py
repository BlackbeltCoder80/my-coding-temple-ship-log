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
#Question =
