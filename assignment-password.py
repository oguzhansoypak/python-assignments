user_name = "oguzhan"

enter_name = input("Please enter your name: ")

if enter_name.lower() == user_name :
    print("Hello,", user_name.capitalize(), "\b!", end=" ")
    print("The password is: Clarusway")

else :
    print("Hello", enter_name.capitalize(), "\b!", end=" ")
    print("See you later.")

