s = input("Enter a string: ")
letter = input("Enter a letter: ")

count = 0

for i in s:
    if i == letter:
        count += 1

print("Frequency:", count)
