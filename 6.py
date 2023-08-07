n = int(input("Enter a positive integer: "))
m = int(input("Enter another positive integer: "))
d = n
c = m
while c != 0: 
    r = d % c
    d = c
    c = r
print("The greatest common divisor of", n, "and", m, "is", d)