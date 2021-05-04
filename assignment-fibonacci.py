fibonacci = [1]

i = 1
count = 0

while i <= 55 :
    fibonacci.append(i)

    i += fibonacci[count]
    count += 1

print(fibonacci)