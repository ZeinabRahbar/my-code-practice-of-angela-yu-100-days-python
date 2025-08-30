
def is_prime(number):

    prime = True

    if number ==1 or number ==0:
        prime = False
    else:
        for i in range(2, 1+ number//2):
            
            if number % i == 0:
                prime = False
                break
            
    return prime


def check_prime():
    number = int(input("Enter the number: "))
    prime = is_prime(number)
    if not prime:
        print(f'the {number} is not prime')
    else:
        print(f'the {number} is prime')


def main():
    check_prime()


main()    

    
    
