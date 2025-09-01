def format_name(f_name, l_name):
    """
    input: first name, last name
    output = result: the 'full name'
    """
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name  = f_name.title()
    formated_l_name = l_name.title()
    return  f"result:{formated_f_name} {formated_l_name}"

print(format_name(input("What is your name? "), input("What is your last name ?")))


#day 10.1

