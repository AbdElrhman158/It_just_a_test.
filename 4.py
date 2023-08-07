plate = input("Enter a li.p: ")

if len(plate) == 6 and plate[:3].isupper() and plate[3:].isdigit():
    print("old.")
elif len(plate) == 7 and plate[:3].isupper() and plate[4:].isdigit():
    print("new")
else:
    print("error.")
