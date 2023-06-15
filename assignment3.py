print("Enter your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponent")
print("7. Modulas")
ch=int(input())
if ch == 1:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The addition of num 1 and num 2 is",n1+n2)
elif ch == 2:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The subtraction of num 1 and num 2 is",n1-n2)
elif ch == 3:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The multiplication of num 1 and num 2 is",n1*n2)
elif ch == 4:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The division of num 1 and num 2 is",n1/n2)
elif ch == 5:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The floor division of num 1 and num 2 is",n1//n2)
elif ch == 6:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The exponent of num 1 and num 2 is",n1**n2)
elif ch == 7:
    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))
    print("The modulas of num 1 and num 2 is",n1%n2)
else:
    print("Invalid choice")


