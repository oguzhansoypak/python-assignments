print("*****************************************")
print("Welcome to the program")
print("You can check if any year is a leap year")
print("*****************************************")

while True :
    print("Type 'q' to exit the program!")
    year = input("Please enter a year: ")

    if year.lower() == "q" :
        print("Exiting the program...")
        break
    
    elif not(year.isnumeric()) :
        print("Invalid entry!")

    else :
        if int(year) % 400 == 0 :
            print(year, "is a leap year")

        elif int(year) % 100 == 0 :
            print(year, "is not a leap year")

        elif int(year) % 4 == 0 :
            print(year, "is a leap year")

        else :
            print(year, "is not a leap year")