import random

name = input("Give me everybodeys name. seperated by comma. ")
names = name.split(", ")

i = random.randint(0, len(names)-1 )
print(names[i], " is going to pay!!!!!!!!!!!")
