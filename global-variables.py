#Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.

x = "bob" 

def call_name():
    print("Hello my name is jhon and this is my friend " + x)


call_name()


"""The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""


def call_name_second():
    global y 
    y = "alex"

call_name_second()
print("my name is " + y) 


# We can also change the value of a global variable inside a function, refer to the variable by using the global keyword:

g = "bob"
def call_name_third():
    global g
    g = "rick"  # here "bob" is replaced with "rick"

call_name_third()
print("my name is " + g) # my name is rick


