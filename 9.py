def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    next = n + 1
    while not is_prime(next):
        next = next + 1
    return next

def main():
    num = int(input("Enter an integer: "))
    result = next_prime(num)
    print("The next prime number after", num, "is", result)

if __name__ == "__main__":
    main()
