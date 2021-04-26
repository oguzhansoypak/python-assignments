print("***************************************")
print("You can check with this program")
print("if a number is an Armstrong number.")
print("***************************************")

number = input("Please enter a positive integer number: ")
int_check = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

while True :
     if set(number).issubset(int_check) :
          break

     else :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
          number = input("Please enter a positive integer number: ")


number_list = list(number)
n_power_sum = 0

for i in number_list :
     n_power_sum += int(i)**len(number_list)

if int(number) == n_power_sum :
     print(number, "is an Armstrong number")

else :
     print(number, "is not an Armstrong number")