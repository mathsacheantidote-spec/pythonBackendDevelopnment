num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter Operator : ")
if op == "+":
    print("The sum of two numbers is:" ,num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "%":
    print(num1%num2)
elif op == "^":
    print(num1^num2)
else :
    print("Invalid Operator")