Number= int(input("Enter the number: "))


count = 0

while Number != 0:

    Number = Number // 10

    count = count + 1

print("Number of digits: " , count)