"""
Python Booleans 

Booleans represent one of two values : True or False.

Boolean Values 


In programming we often need to know if an expression is Ture or False.
We can Evaluate any expression in Python, and get one of two answers, True or False. 

When we compare two values, the Expression is evaluated and Python returns the Boolean answer: 

"""

print(10 > 9) # This will return True. 

print(10 == 9) # Returns False. 

print(10 < 9) # Returns False.


# When we run a condition in an if statement, Python returns True or Flase: 

a = 200 
b = 33 

if b > a:
    print("b is greater than a")
else: 
    print("b is not greater than a")

# The above if else condition will return ("b is not greater than a")

# Evaluate Values and Variables. 
# The bool() function allows us to evaluate any value, and give us True or False in return. 

# Evaluate a string and a number:- 

print(bool("Hello"))
print(bool(15))

# Evaluate two values:-

x = "Hello"
y = 15 

print(bool(x))
print(bool(y))


# Most values are True 
"""
Almost any value is evaluated to True if it has some sort of content. 

Any string is True, except empty strings.

Any number is True, except 0. 
 
Any list, tuple, set, and dictionary are True, except empty ones. 

"""

# Examples : -

# The following will return True:

bool("abc")
bool(123)
bool(["apple","cherry","orange"])
  


# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# Examples : - 
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean 
# We can create functions that return a Boolean Value: 

# Example: 

def myFunction(): 
    return True

print(myFunction())   # This will Return True as defined in Function named myFunction().

# Example Print "YES!" if the function returns True, otherwise print "NO!": 

def MyFunction(): 
    return True  # if we replace this True with False OR 0 the output will be "NO!" , same goes the other way around. 

if MyFunction(): 
    print("YES!")
else: 
    print("NO!")


# Python also has many built-in functions that return a boolean value, like the "isinstance()" function, which can be used to determine if an object is of a certain data type: 

# Example : - 
x = 100 
print(isinstance(x, int)) # "isinstance()",  Checks whether x = 100 is ACTUALLY OF DATA TYPE INTEGER.
