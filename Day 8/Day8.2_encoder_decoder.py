def decode(message, shift_num):
    str_list = 'abcdefghijklmnopqrstuvwxyz'
    decoded_messgae = ""
    
    for letter in message:
        letter_place = str_list.find(letter)


        if letter in str_list:
            new_letter_place = letter_place - shift_num
            decoded_messgae += str_list[new_letter_place%26]
        else:
          
            decoded_messgae += letter
        
    return decoded_messgae

def encode(message, shift_num):
    str_list = 'abcdefghijklmnopqrstuvwxyz'
    punc_list = ' 0123456789.+-*/+=_-)(*&^%$#@!~|?><:"]},;{["'
    encoded_messgae = ""
    
    for letter in message:
        if letter in str_list:
            
            letter_place = str_list.find(letter)
            new_letter_place = letter_place + shift_num
            encoded_messgae += str_list[new_letter_place%26]

        else:
            encoded_messgae += letter
        

    return encoded_messgae


    
continuation = 'yes'

while continuation != 'no':
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if continuation == 'yes':

        message = input("Type your message, you can just put on lowercase letters nothing else can be accepted:\n").lower()
        shift_num = int(input("Type your shift number:\n"))



        if encode_or_decode == 'encode':


            encoded_message = encode(message, shift_num)
            print(f"Your encoded message is {encoded_message}.")
            

        elif encode_or_decode == 'decode':

            decoded_message = decode(message, shift_num)
            print(f"The decoded message is: {decoded_message}.")


        else:    
            print("your command is not recognized.")
    else:
        print("your printed value was not recognized, you should type 'yes' or no.")

    continuation = input("Type 'yes' if you want to go again. Otherwise type 'no': ")


        
