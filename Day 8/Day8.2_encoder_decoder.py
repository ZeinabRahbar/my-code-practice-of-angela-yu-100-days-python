def is_all_lower_alpha(text):
    # Returns True if text contains only lowercase letters a-z
    return text.isalpha() and text.islower()

def decode(message, shift_num):
    str_list = 'abcdefghijklmnopqrstuvwxyz'
    decoded_messgae = ""
    
    for letter in message:
        letter_place = str_list.find(letter)
        new_letter_place = letter_place - shift_num
        decoded_messgae += str_list[new_letter_place%26]
        
    return decoded_messgae

def encode(message, shift_num):
    str_list = 'abcdefghijklmnopqrstuvwxyz'
    encoded_messgae = ""
    
    for letter in message:
        letter_place = str_list.find(letter)
        new_letter_place = letter_place + shift_num
        encoded_messgae += str_list[new_letter_place%26]    

    return encoded_messgae


    
continuation = 'yes'

while continuation != 'no':
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if continuation == 'yes':

        message = input("Type your message, you can just put on lowercase letters nothing else can be accepted:\n")
        shift_num = int(input("Type your shift number:\n"))



        if encode_or_decode == 'encode':


            if is_all_lower_alpha(message) == True:
                encoded_message = encode(message, shift_num)
                print(f"Your encoded message is {encoded_message}.")

            else:
                
                print("please do not input anything but the lower case letter, not even a space")

                

        elif encode_or_decode == 'decode':


            if is_all_lower_alpha(message) == True:

                decoded_message = decode(message, shift_num)

                print(f"The decoded message is: {decoded_message}.")
            
            else:
                print("please do not input anything but the lower case letter, not even a space")


        else:    
            print("your command is not recognized.")
    else:
        print("your printed value was not recognized, you should type 'yes' or no.")

    continuation = input("Type 'yes' if you want to go again. Otherwise type 'no': ")


        
