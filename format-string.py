"""
We cannot combine strings and numbers like this:- 

age = 10

txt = "My name is jhon, I am " + age

print(txt)

the above line of code will give a ERROR 

But we can combine Strings and Numbers using the f-strings or the format() method. 


# F STRINGS 

f-string was introduced in python 3.6, and is now the preferred way of formatting strings. 
to specify a string as an f-string, simply put an "f" in the front of the string literal, and add curly brackets {} as placeholders for variables and other operations.


"""


# EXAMPLE OF AN F-STRING :- 

age = 10 
txt = f"My name is Jhon, I am {age} years old."
print(txt)

# Place-Holders and Modifiers 

# A place holder can contain variables, operations, fucntions, and modifiers to format the value. 

# Example Adding a place holder for the "price" variable:- 

price = 59
txt = f"The price is {price} rupees."
print(txt)

# A place-holder can include a modifier to format the value, a modifier is included by adding a colon ":" followed by a legal formatting type, like ".2f" which means fixed point number with 2 decimals:-

# DISPLAYING THE PRICE WITH 2 DECIMALS:- 

price = 59 
txt = f"The price is {price:.2f} rupees."
print(txt)

# OUTPUT - "59.00"

# A place-holder contain and perform math operations:-

txt = f"The price is {20 * 59} rupees."
print(txt)

# OUTPUT - "The price is 1180 rupees."