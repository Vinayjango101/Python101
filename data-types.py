#-------------------------------------------------------------------------------------------------------
# TEXT TYPE DATA TYPE
name = str("bob")  # this is a string type or str

print(name)
#-------------------------------------------------------------------------------------------------------
#NUMERIC TYPE DATA TYPE 
age = int(17) # this is a integer type or int

print(age)

weight = float(71.5) # this is a float type

print(weight)

nums = complex(3, 4j) # it has a real part i.e '3' and imaginary part '4j' , can also be created using direct method like z1 = 3 + 4j

print(nums)
#-------------------------------------------------------------------------------------------------------
#SEQUENCE TYPE DATA TYPE 

allowed_names = ["bob","alex","jhon"] # this is a list type

print(allowed_names)

good_names = ("jake","nathan","jura") # this is a tuple type

print(good_names)

x = range(10) # this is a range type, it will return/print every number within the range 0-10 

print(x)
#-------------------------------------------------------------------------------------------------------
# MAPPING TYPE DATA TYPE 

a = {"name" : "sully", "age" : "17"} # this is a dictionary / dict type

print(a)
#-------------------------------------------------------------------------------------------------------
# SET TYPE DATA TYPE 

h = {"tiger","lion","elephant"} # this is a set type its elements can be modified using add(), update(), remove(), discard(), pop()
# for example :- 
h.add("panda") 
print(h)


goals_scored = frozenset({"100","500","900"}) # this is a frozen set type its elements cannot be modified like the set type
#-------------------------------------------------------------------------------------------------------

# BOOLEAN TYPE DATA TYPE
# these are either True or False
looped = True # type true 
notlooped = False # type false

print(looped, notlooped)

#-------------------------------------------------------------------------------------------------------

# BYTE TYPE DATA TYPE 
d = bytes(5)
#display d:
print(d)
print(type(d))

#-------------------------------------------------------------------------------------------------------

#BYTE ARRAY TYPE DATA TYPE
g = bytearray(10)
#display g:
print(g)
print(type(g))

#-------------------------------------------------------------------------------------------------------

# MEMORY VIEW TYPE DATA TYPE 

j = memoryview(bytes(8))

#display j:
print(j)
print(type(j))

#-------------------------------------------------------------------------------------------------------


