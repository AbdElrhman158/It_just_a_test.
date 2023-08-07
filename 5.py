message = input("Enter a message: ")
shift = int(input("Enter a shift amount: "))

encoded = ""
for char in message:
    if char.isalpha():
        code = ord(char)
        code += shift
        
        if char.isupper():
            if code > ord("Z"):
                code -= 26
            elif code < ord("A"):
                code += 26
        elif char.islower():
            if code > ord("z"):
                code -= 26
            elif code < ord("a"):
                code += 26
        char = chr(code)
    encoded += char
print("The encoded message is:", encoded)
