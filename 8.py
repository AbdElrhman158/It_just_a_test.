def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    num = int(input("Enter an integer: "))
    result = is_prime(num)
    if result:
        print(num, "is a prime number.")
    else:

        print(num, "is not a prime number.")
if __name__ == "__main__":
    main()