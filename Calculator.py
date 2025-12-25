def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
n=int(input("Enter your choice: "))
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if n==1:
    print("Sum: ",add(a,b))
elif n==2:
    print("Difference: ",sub(a,b))
elif n==3:
    print("Product: ",mul(a,b))
elif n==4:
    print("Quotient: ",div(a,b))
else:
    print("Invalid choice")