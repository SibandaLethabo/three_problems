def simple_calculator (num1, num2 , operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        return num1 + num2
    if operator == "*":
        return num1 * num2 
    if operator == "/":
        if num1 >= num2:
            return int(num1 / num2) 
        else:
            return int(num2 / num1)
    if operator == "-":
        if num1 >= num2:
            return num1 - num2 
        else:
            return num2 - num1
num1 = input("Enter first number:")
num2 = input("Enter second number:")
operator = input("Enter operator (+, -, *, /):")
print(simple_calculator(num1, num2, operator))        