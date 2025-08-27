import random

print("Welcome to the password generator")

letter_num = int(input("How nany letters would you like in your password? "))
symbol_num = int(input("How nany symbols would you like in your password? "))
number_bum = int(input("How nany numbers would you like in your password? "))


string_pick = "abcdefghijklmnopqrstuwxyz"
number_pick = "12345678910"
symbol_pick = "!@$%^&*()_-=+/"

password = ""

for i in range(letter_num):
    password += string_pick[random.randint(0,len(string_pick)- 1)]

for i in range(symbol_num):
    password += symbol_pick[random.randint(0,len(symbol_pick)- 1)]

for i in range(number_bum):
    password += number_pick[random.randint(0,len(number_pick)- 1)]


print(f"Hear is your password {password}")

new_pass = []


for i in password:
    new_pass.append(i)

random.shuffle(new_pass)


new_password = ""
for i in new_pass:
    new_password += i

print(f"Hear is your shuffled password {new_password}")
