print("*********************************************")
print("Welcome to covid-19 risky group test!")
print("Please answer the questions with 'yes or no'!")
print("*********************************************")

age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune = input("Is your immune system too weak? ")



if age.lower() == "yes" or chronic.lower() == "yes" or immune.lower() == "yes" :
    print("You are in risky group!")

elif age.lower() == "no" and chronic.lower() == "no" and immune.lower() == "no" :
    print("You are not in risky group!")