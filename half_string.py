s = input("Enter a string: ")

half = len(s) // 2
result = s[:half].upper() + s[half:]

print(result)
