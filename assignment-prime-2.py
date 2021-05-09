n = int(input("Please enter a number: "))
prime_list = []


for i in range(1, n+1) :
    count = 0

    for j in range(1, i+1) :
        if i % j == 0 :
            count += 1

    if count == 2 :
        prime_list.append(i)

print(f"List of prime numbers from 1 to {n}: {prime_list}")