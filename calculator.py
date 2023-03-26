def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def divison(x,y):
    return x / y

print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.divison')

result = input("Please select an operation (addition/subtraction/multiplication/division: ")
number1 = float(input("Please select the first number: "))
number2 = float(input("Please select the second number : "))

if result == 'addition':
    print(number1 , '+' , number2 , '=' , addition(number1, number2))
elif result == 'subtraction':
    print(number1 , '-' , number2 , '=' , subtraction(number1, number2))
elif result == 'multiplication':
    print(number1 , '*' , number2 , '=' , multiplication(number1, number2))
elif result == 'divison':
    print(number1 , '/', number2 , '=', divison(number1, number2))
else:
    print("invalid operation !")


