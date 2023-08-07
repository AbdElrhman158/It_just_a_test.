decimal = int(input("Enter a decimal number: "))
result = ""
while decimal > 0:
    r = decimal % 2
    result = str(r) + result
    decimal = decimal // 2
    print("The binary number is:", result)
