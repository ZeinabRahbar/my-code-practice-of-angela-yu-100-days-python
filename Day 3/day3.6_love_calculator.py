print("Welcome to love Calculator!!!")

name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2

count = 0

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = str(true) + str(love)

love_score = int(love_score)


if love_score <10 or love_score> 90:
    print(f"Your love_score is {love_score}!, you go together!!!")

elif love_score>= 40 and love_score<= 50:
        print(f"Your love_score is {love_score}!, you are alright!!!")

else:
    print(f"Your score is {love_score}, get over him/her")

