# Strings in python are surrounded by either single quotes or double quotes 
# 'hello'  is the same as "hello"

# We can display a string literal with the print() function.

print('hello')
print("hello")


#---------------------------------------------------------------------------------------
 
# Quotes inside Quotes 
# We can use quotes inside a string as long as they dont match the quotes surrounding the string:-

print("It's Alright")
print(' they said "THANK YOU !" ')

#---------------------------------------------------------------------------------------

# Assign a String to a Variable 
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:-
a = "test123"
print(a)

#---------------------------------------------------------------------------------------

# Multiline String
# We can assign a multiline string to a variable by using three quotes 

k = """
hello my name is jhon 
i love to play playstation, 
i love to code aswell ! :D 

"""

print(k)

# OR also by using three single quotes 

o = '''
hello myself mat , i love to play 
in swimming pool , i also enjoy 
painting ! :3

'''

print(o)
#---------------------------------------------------------------------------------------

# Strings as Arrays 

#Like many other popular programming languages, strings in Python are arrays of unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.

r = "Hello, World!"

print(r[0]) # this will only print the character that has position 0 i.e "H"

# So its print(variable_name[element_position_number])

#---------------------------------------------------------------------------------------

# Looping through a String

for x in "tiger":
    print(x) # Looping through the word 'tiger'


#---------------------------------------------------------------------------------------

# String Length 

# To get the length of a string using the len() function: 

t = "Hello, World!"
print(len(t))

#---------------------------------------------------------------------------------------

# Check String 

# To check whether the word or number is present in the string 

txt1 = "The best things in life are free !"

print("free" in txt1) # this is print True as free is present in the variable named txt1


# Check string using IF

txt2 = "The best things in life are free !"
if "free" in txt2:
    print("Yes, 'free' is present.")

#---------------------------------------------------------------------------------------

# Check if "expensive" is NOT present in the following text:

txt3 = "The best things in life are free!"
print("expensive" not in txt3) # this is print True as expensive is not present in the variable named txt3


# Use it in an if statement:

#print only if "expensive" is NOT present:

txt4 = "The best things in life are free!"
if "expensive" not in txt4:
  print("No, 'expensive' is NOT present.")


#---------------------------------------------------------------------------------------