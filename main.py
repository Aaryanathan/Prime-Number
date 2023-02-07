num = int(input("Enter a Number: "))

if num == 1:
    print("It is neither prime nor composite")
elif num == 2:
    print("It is a prime number")

else:
    isprime = True
    for i in range(2, num):

        if num % i == 0:
            isprime = False
            break
        
        elif num % i != 0:
            isprime = True
    if isprime == True:
        print("It is a prime number")
    else:
        print("It is not a prime number")