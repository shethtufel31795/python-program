num = input("Enter a number: ")

even = 0
odd = 0

for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digits:", even)
print("Odd digits:", odd)
