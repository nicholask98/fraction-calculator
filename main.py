def addition(num_1, num_2, denom_1, denom_2):
    print('addition')
    common_denom = denom_1 * denom_2
    num_1 *= denom_2
    num_2 *= denom_1
    num_sum = num_1 + num_2

# FIXME: Find out how to find GCD and LCM


def subtraction(num_1, num_2, denom_1, denom_2):
    print('subtraction')
# FIXME: 


def multiplication(num_1, num_2, denom_1, denom_2):
    print('multiplication')
# FIXME: 


def division(num_1, num_2, denom_1, denom_2):
    print('division')
# FIXME: 




user_input = input("Enter a fraction calculation (operators: + - * /)(Format: x/y + a/b)\n")

operator = list(user_input.split())[1]

# Each variable as integers
num_1 = int(list(user_input.split())[0].split('/').pop(0))
num_2 = int(list(user_input.split())[2].split('/').pop(0))
denom_1 = int(list(user_input.split())[0].split('/').pop())
denom_2 = int(list(user_input.split())[2].split('/').pop())

if operator == '+':
    addition(num1, num_2, denom_1, denom_2)
elif operator == '-':
    subtraction(num1, num_2, denom_1, denom_2)
elif operator == '*':
    multiplication(num1, num_2, denom_1, denom_2)
elif operator == '/':
    division(num1, num_2, denom_1, denom_2)
else:
    print("Error. Invalid operator.")