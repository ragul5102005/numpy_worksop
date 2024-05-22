#write a program to find if the given number is prime no or not
def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True

number = 29  
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
