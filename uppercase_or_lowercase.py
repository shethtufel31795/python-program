def check_string(s):
    if len(s) > 5:
        print(s.upper())
    else:
        print(s.lower())

text = input("Enter a string: ")
check_string(text)
