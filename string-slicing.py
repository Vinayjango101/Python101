
#--------------------------------------------------------------------------------------------------------------------
#Slicing 
#You can return a range of characters by using the slice syntax.

#Specify the start index and the end index, separated by a colon, to return a part of the string.

a = "Hello World!"

print(a[2:5])  
#--------------------------------------------------------------------------------------------------------------------

#Slice From the start 

#By Leaving out the start index, the range will start at the first character 

b = "Hello World!"
print(b[:5])

#--------------------------------------------------------------------------------------------------------------------

# Slice to the end

#Get the characters from position 2, and all the way to the end 
z = "Hello World!"
print(z[2:])

#--------------------------------------------------------------------------------------------------------------------

# Negative Indexing 

# Use negative indexes to start the slice from the end of the string 

# get the characters from "o" in World! (position -5) To, but not included "d" in World !(position -2)

f = "Hello World!"
print(f[-5:-2])

#--------------------------------------------------------------------------------------------------------------------







