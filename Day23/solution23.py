def calculator():
    try:
        num1=float(input('Enter first Number: '))
        op=input("Enter operator (+, -, *, /): ")
        num2=float(input('Enter second Number: '))

        if op == '+':
            result=num1+num2
        elif op == '-':
            result=num1-num2
        elif op == '*':
            reult=num1*num2
        elif op == '/':
            reult=num1/num2
        else:
            print('Invalid Operator')
            return
        print("Result:", result)

    except ZeroDivisionError:
        print('Error. Cannot divide by zero')
    except ValueError:
        print("Error: Please enter valid numbers.")
    except NameError:
        print("Error: Undefined variable used.")

calculator()