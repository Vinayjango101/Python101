#Python Does not have a random() function it can be made possible with the use of a built-in module named random 

import random

print(random.randrange(1,10))



# we can also get a random choice of str and other data type 

names = {"bob","alex","jake"}

random_names = random.choice(list(names))
print(random_names)