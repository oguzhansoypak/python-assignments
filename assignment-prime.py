print("*******************************")
print("Welcome to prime number check!")
print("*******************************")


while True :
    num = input("Please enter a number(Type 'q' to exit the program!): ")

    if num.lower() == "q" :
        print("Exiting the program...")
        break

    elif not num.isnumeric() :
        print("Invalid entry! Please enter a positive integer number!")

    elif int(num) > 1 :
        prime = True

        for i in range(2, int(num)) :
            if int(num) % i == 0 :
                prime = False
                break

        if prime :
            print(num, "is a prime number!")

        else :
            print(num, "is not a prime number!")

    else :
        print("Only integer numbers greater than one can be prime numbers!")