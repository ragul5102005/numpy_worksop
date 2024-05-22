#write a program to find the sum of digits of a given number'
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


number = 687
print("Sum of digits:", sum_of_digits(number))  
