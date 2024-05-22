# find if the given number is a palindrome or not?
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
