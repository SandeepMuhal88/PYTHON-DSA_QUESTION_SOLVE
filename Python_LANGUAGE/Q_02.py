num=int(input("Enter a number to check number is prime and not Prime:-"))

def isPrime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True

print(isPrime(num))




