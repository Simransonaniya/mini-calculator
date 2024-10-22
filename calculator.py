#calculator
operator=input("enter an operator(+ - * /):")
num1=float(input("enter 1st no:"))
num2=float(input("enter 2nd no:"))

if operator =="+":
    result=num1+num2
    print(result)
elif operator =="-":
    result=num1-num2
    print(result)
elif operator =="*":
    result=num1*num2
    print(result)
elif operator =="/":
    result=num1/num2
    print(result)
else:
    print(default)

