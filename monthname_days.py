month = input("Enter month name: ").lower()

if month in ["january","march","may","july","august","october","december"]:
    print("31 days")
elif month in ["april","june","september","november"]:
    print("30 days")
elif month == "february":
    print("28 or 29 days")
else:
    print("Invalid month")
